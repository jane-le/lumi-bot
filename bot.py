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

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(os.environ['SIGNING_SECRET'], '/slack/events', app)
client = slack.WebClient(token=os.environ['SLACK_TOKEN'])
BOT_ID = client.api_call("auth.test")['user_id']

@slack_event_adapter.on('message')
def message(payload):
    print("Hello")
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
    client.chat_postMessage(channel=data.get('channel_id'), text="What is your favourite colour?")
    return Response(), 200

@app.route('/set-icebreakers', methods=['POST'])
def make_icebreakers():
    data = request.form

    open_dialog = client.dialog_open(dialog=constants.DIALOG_FORM,trigger_id=data.get("trigger_id"))
    #client.chat_postMessage(channel=data.get('channel_id'), user=data.get('user_id'), text=SCHEDULE_FORM_TITLE,attachments=SCHEDULE_FORM)
    return Response(), 200

@app.route('/slack/interactive-endpoint', methods=['POST'])
def set_icebreakers():
    data = json.loads(request.form.get('payload'))
    client.chat_postEphemeral(channel=data['channel']['id'], user=data['user']['id'], text=constants.SCHEDULE_ICEBREAKERS_CONFIRMATION)
    schedule_icebreakers()
    return Response(), 200

def get_username(data):
    return client.users_info(user=data.get('user_id')).get("user").get("profile").get("first_name")

def schedule_icebreakers(): 
    ids = []
    for msg in constants.SCHEDULED_MESSAGES: 
        response = client.chat_scheduleMessage(channel=msg['channel'], text=msg['text'], post_at=msg['post_at'])
        id_ = response.get('scheduled_message_id')
        ids.append(id_)
    print (client.chat_scheduledMessages_list(channel="C0216QC0JQ3"))

if __name__ == "__main__":
    #schedule_icebreakers(SCHEDULED_MESSAGES)
    app.run(debug=True)