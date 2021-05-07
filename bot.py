import slack
import os
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask, request, Response
from slackeventsapi import SlackEventAdapter
from datetime import datetime, timedelta
import time

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(os.environ['SIGNING_SECRET'], '/slack/events', app)
client = slack.WebClient(token=os.environ['SLACK_TOKEN'])
BOT_ID = client.api_call("auth.test")['user_id']

SCHEDULED_MESSAGES = [
    {'text': 'Hi', 'post_at': (datetime.now() + timedelta(seconds=30)).timestamp(), 'channel': 'C0216QC0JQ3'},
]

@slack_event_adapter.on('message')
def message(payload):
    event = payload.get('event', {})
    channel_id = event.get('channel')
    user_id = event.get('user')
    text = event.get('text')
    
    if BOT_ID != user_id:
        client.chat_postMessage(channel=channel_id, text=text)


@app.route('/queue', methods=['POST'])
def queue_question():
    data = request.form
    bot_response = "Thanks {name}! I'll add it to the queue :smiley_cat:".format(name=get_username(data))
    client.chat_postEphemeral(channel=data.get('channel_id'), user=data.get('user_id'), text=bot_response)
    return Response(), 200

@app.route('/icebreaker', methods=['POST'])
def icebreaker():
    data = request.form
    client.chat_postMessage(channel=data.get('channel_id'), text="What is your favourite colour?")
    return Response(), 200

def get_username(data):
    return client.users_info(user=data.get('user_id')).get("user").get("profile").get("first_name")

def schedule_icebreakers(icebreakers): 
    ids = []
    for msg in SCHEDULED_MESSAGES: 
        response = client.chat_scheduleMessage(channel=msg['channel'], text=msg['text'], post_at=msg['post_at'])
    id_ = response.get('id')
    ids.append(id_)
    return ids

if __name__ == "__main__":
    schedule_icebreakers(SCHEDULED_MESSAGES)
    app.run(debug=True)