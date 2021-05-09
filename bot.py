import slack
import os
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask, request, Response, make_response
from slackeventsapi import SlackEventAdapter
from datetime import datetime, timedelta
import time
import json

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(os.environ['SIGNING_SECRET'], '/slack/events', app)
client = slack.WebClient(token=os.environ['SLACK_TOKEN'])
BOT_ID = client.api_call("auth.test")['user_id']

SCHEDULED_MESSAGES = [
    {'text': 'Hi', 'post_at': (datetime.now() + timedelta(seconds=30)).timestamp(), 'channel': 'C0216QC0JQ3'},
]

DIALOG_FORM = {
    "title": "Set Lumi's Icebreakers!",
    "submit_label": "Submit",
    "callback_id": "icebreaker_form",
    "elements": [
        {
            "label": "How often? Every: ",
            "type": "select",
            "name": "frequency",
            "placeholder": "Day",
            "options": [
                {
                    "label": "Weekday",
                    "value": "weekday"
                },
                {
                    "label": "Day",
                    "value": "day"
                },
            ]
        },
    ]
}
SCHEDULE_FORM_TITLE = "Let's configure your icebreakers! :smile_cat:"
SCHEDULE_FORM = [
    {
        "text": "Step :one: : Choose your frequency!",
        "fallback": "You are unable to choose a game",
        "callback_id": "freq_selection",
        "color": "#2ba197",
        "attachment_type": "default",
        "actions": [
            {
                "name": "game",
                "text": "Weekdays",
                "type": "button",
                "value": "weekday"
            },
            {
                "name": "game",
                "text": "Everyday",
                "type": "button",
                "value": "day"
            }
        ]
    },
    {
        "text": "Step :two::  Choose what time to display your icebreakers!",
        "fallback": "If you could read this message, you'd be choosing something fun to do right now.",
        "color": "#2ba197",
        "attachment_type": "default",
        "callback_id": "time_selection",
        "actions": [
            {
                "name": "games_list",
                "text": "Pick a game...",
                "type": "select",
                "options": [
                    {
                        "text": "12:00 AM",
                        "value": 0
                    },
                    {
                        "text": "1:00 AM",
                        "value": 1
                    },
                    {
                        "text": "2:00 AM",
                        "value": 2
                    },
                    {
                        "text": "3:00 AM",
                        "value": 3
                    },
                    {
                        "text": "4:00 AM",
                        "value": 4
                    },
                    {
                        "text": "5:00 AM",
                        "value": 5
                    },
                    {
                        "text": "6:00 AM",
                        "value": 6
                    },
                    {
                        "text": "7:00 AM",
                        "value": 7
                    },
                    {
                        "text": "8:00 AM",
                        "value": 8
                    },
                    {
                        "text": "9:00 AM",
                        "value": 9
                    },
                    {
                        "text": "10:00 AM",
                        "value": 10
                    },
                    {
                        "text": "11:00 AM",
                        "value": 11
                    },
                    {
                        "text": "12:00 PM",
                        "value": 12
                    },
                    {
                        "text": "1:00 PM",
                        "value": 13
                    },
                    {
                        "text": "2:00 PM",
                        "value": 14
                    },
                    {
                        "text": "3:00 PM",
                        "value": 15
                    },
                    {
                        "text": "4:00 PM",
                        "value": 16
                    },
                    {
                        "text": "5:00 PM",
                        "value": 17
                    },
                    {
                        "text": "6:00 PM",
                        "value": 18
                    },
                    {
                        "text": "7:00 PM",
                        "value": 19
                    },
                    {
                        "text": "8:00 PM",
                        "value": 20
                    },
                    {
                        "text": "9:00 PM",
                        "value": 21
                    },
                    {
                        "text": "10:00 PM",
                        "value": 22
                    },
                    {
                        "text": "11:00 PM",
                        "value": 23
                    }
                ]
            }
        ]
    }
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

@app.route('/set-icebreakers', methods=['POST'])
def schedule_icebreakers():
    data = request.form
    print(data)
    # Show the ordering dialog to the user
    # """open_dialog = client.dialog_open(dialog=DIALOG_FORM,trigger_id=data.get("trigger_id"),) """
    client.chat_postMessage(channel=data.get('channel_id'), user=data.get('user_id'), text=SCHEDULE_FORM_TITLE,attachments=SCHEDULE_FORM)
    return Response(), 200

@app.route('/slack/interactive-endpoint', methods=['POST'])
def set_icebreakers():
    data = json.loads(request.form.get('payload'))
    print(data['message_ts'])
    if data['attachment_id'] == '2':
        client.chat_update(channel=data['channel']['id'], ts=data['message_ts'], text="thanks!", attachments=[])
   # client.chat_postEphemeral(channel=data.get('channel').get, user=data.get('user_id'), text=bot_response)
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
    #schedule_icebreakers(SCHEDULED_MESSAGES)
    app.run(debug=True)