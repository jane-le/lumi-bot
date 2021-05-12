import slack
import os
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask, request, Response, make_response
from slackeventsapi import SlackEventAdapter
import time
import json
import logging
import constants
import datetime
import questions
import random
import asyncio

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(os.environ['SIGNING_SECRET'], '/slack/events', app)
client = slack.WebClient(token=os.environ['SLACK_TOKEN'])
BOT_ID = client.api_call("auth.test")['user_id']
freq = "day"
set_time = "0"
schedule_in_progs = False

@slack_event_adapter.on('member_joined_channel')
def welcome_msg(payload):
    event = payload.get('event', {})
    channel_id = event.get('channel')
    print(payload)
    print("IM IN")
    client.chat_postMessage(channel=channel_id, text=constants.LUMI_CHANNEL_JOIN_MSG)

@slack_event_adapter.on('message')
def message(payload):
    global set_time
    global freq
    global schedule_in_progs
    event = payload.get('event', {})
    channel_id = event.get('channel')
    print(payload)
    if (event.get('text') == constants.SCHEDULING_MESSAGES_TEXT and not schedule_in_progs ):
        print("hello")
        schedule_icebreakers(channel_id=channel_id)
        time_hr = datetime.datetime.strptime(set_time, "%H")
        client.chat_update(channel=channel_id, ts=event.get('ts'), text=constants.SCHEDULE_ICEBREAKERS_CONFIRMATION.format(freq=freq, time=time_hr.strftime("%I:%M %p")))
    if (event.get('subtype') == 'channel_join' and BOT_ID == event.get('user')): 
        print("hi")
        client.chat_postMessage(channel=channel_id, text=constants.LUMI_CHANNEL_JOIN_MSG)
    
@app.route('/icebreaker', methods=['POST'])
def icebreaker():
    data = request.form
    client.chat_postMessage(channel=data.get('channel_id'), text=get_icebreaker_msg())
    return Response(), 200

@app.route('/set-icebreakers', methods=['POST'])
def make_icebreakers():
    data = request.form
    client.dialog_open(dialog=constants.DIALOG_FORM,trigger_id=data.get("trigger_id"))
    return Response(), 200

@app.route('/slack/interactive-endpoint', methods=['POST'])
def set_icebreakers():
    global freq 
    global set_time

    data = json.loads(request.form.get('payload'))
    freq = data['submission']['frequency']
    set_time = data['submission']['time']
    
    client.chat_postMessage(channel=data['channel']['id'], text=constants.SCHEDULING_MESSAGES_TEXT)
    return Response(), 200 

def get_username(data):
    return client.users_info(user=data.get('user_id')).get("user").get("profile").get("first_name")

def schedule_icebreakers(channel_id: str): 
    global freq 
    global set_time
    global schedule_in_progs 
    schedule_in_progs = True
    
    #delete all prev scheduled messages
    schedule_messages = client.chat_scheduledMessages_list(channel=channel_id).get('scheduled_messages')
    for x in schedule_messages:
        try:
            client.chat_deleteScheduledMessage(channel=channel_id, scheduled_message_id=x['id'])
        except: 
            print(x['id'])

    today = datetime.datetime.now()
    curr_date = datetime.datetime(today.year, today.month, today.day, int(set_time))
    is_weekday = freq == "weekday"

    if (curr_date < today):
        curr_date = curr_date + datetime.timedelta(days=1)

    for i in range(0, constants.MAX_FUTURE_DAYS_CAP-1):
        if (not(is_weekday and curr_date.weekday() > 5)):
            message_text = get_icebreaker_msg()
            client.chat_scheduleMessage(channel=channel_id, text=message_text, post_at=curr_date.timestamp())
            curr_date = curr_date + datetime.timedelta(days=1)
    schedule_in_progs = False

def get_icebreaker_msg():
    questions_length = len(questions.ICEBREAKERS)
    greetings_length = len(constants.LUMI_QUESTION_GREETINGS)
    return constants.LUMI_QUESTION_GREETINGS[random.randint(0,greetings_length-1)].format(question=questions.ICEBREAKERS[random.randint(0,questions_length-1)])

if __name__ == "__main__":
    app.run(debug=True)