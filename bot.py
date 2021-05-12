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

@slack_event_adapter.on('message')
def message(payload):
    print("Hello")
    print(payload)
   # event = payload.get('event', {})
  #  channel_id = event.get('channel')
  #  user_id = event.get('user')
  #  text = event.get('text')

  #  if BOT_ID != user_id:
   #     client.chat_postMessage(channel=channel_id, text=text)


@app.route('/queue', methods=['POST'])
def queue_question():
    data = request.form
    bot_response = constants.QUEUE_QUESTION_RESPONSE.format(name=get_username(data))
    client.chat_postEphemeral(channel=data.get('channel_id'), user=data.get('user_id'), text=bot_response)
    return Response(), 200

@app.route('/icebreaker', methods=['POST'])
def icebreaker():
    data = request.form
    questions_length = len(questions.ICEBREAKERS)
    greetings_length = len(constants.LUMI_QUESTION_GREETINGS)
    client.chat_postMessage(channel=data.get('channel_id'), text=constants.LUMI_QUESTION_GREETINGS[random.randint(0,greetings_length-1)].format(question=questions.ICEBREAKERS[random.randint(0,questions_length-1)]))
    return Response(), 200

@app.route('/set-icebreakers', methods=['POST'])
def make_icebreakers():
    data = request.form
    client.dialog_open(dialog=constants.DIALOG_FORM,trigger_id=data.get("trigger_id"))
    return Response(), 200

@app.route('/slack/interactive-endpoint', methods=['POST'])
def set_icebreakers():
    data = json.loads(request.form.get('payload'))
    is_weekday =  data['submission']['frequency'] == 'weekday'
    freq = is_weekday
       # schedule_icebreakers(data['channel']['id'], is_weekday, int(data['submission']['time']))
    
    user_name = client.users_info(user=data['user']['id']).get("user").get("profile").get("first_name")

    time_hr = datetime.datetime.strptime(data['submission']['time'], "%H")
    
    client.chat_postMessage(channel=data['channel']['id'], text=constants.SCHEDULING_MESSAGES_TEXT)
    client.chat_postMessage(channel=data['channel']['id'], text=constants.SCHEDULE_ICEBREAKERS_CONFIRMATION.format(user=user_name, freq=data['submission']['frequency'], time=time_hr.strftime("%I:%M %p")))
    return Response(), 200 

def get_username(data):
    return client.users_info(user=data.get('user_id')).get("user").get("profile").get("first_name")

def schedule_icebreakers(channel_id: str, is_weekday: bool, time: int): 
    delete_scheduled_icebreakers(channel_id)
    today = datetime.datetime.now()
    curr_date = datetime.datetime(today.year, today.month, today.day, time)
    questions_length = len(questions.ICEBREAKERS)
    greetings_length = len(constants.LUMI_QUESTION_GREETINGS)

    if (curr_date < today):
        curr_date = curr_date + datetime.timedelta(days=1)

    for i in range(0, constants.MAX_FUTURE_DAYS_CAP-1):
        if (not(is_weekday and curr_date.weekday() > 5)):
            message_text = constants.LUMI_QUESTION_GREETINGS[random.randint(0,greetings_length-1)].format(question=questions.ICEBREAKERS[random.randint(0,questions_length-1)])
            response = client.chat_scheduleMessage(channel=channel_id, text=message_text, post_at=curr_date.timestamp())
            curr_date = curr_date + datetime.timedelta(days=1)
    print("messages are scheduled")

def delete_scheduled_icebreakers(channel_id: str):
    schedule_messages = client.chat_scheduledMessages_list(channel=channel_id).get('scheduled_messages')
    for x in schedule_messages:
        client.chat_deleteScheduledMessage(channel=channel_id, scheduled_message_id=x['id'])
    print(client.chat_scheduledMessages_list(channel=channel_id))

if __name__ == "__main__":
    app.run(debug=True)