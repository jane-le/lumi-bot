from datetime import datetime, timedelta

SCHEDULED_MESSAGES = [
    {'text': 'Msg 1', 'post_at': (datetime.now() + timedelta(minutes=30)).timestamp(), 'channel': 'C0216QC0JQ3'},
    {'text': 'Msg 2', 'post_at': (datetime.now() + timedelta(minutes=60)).timestamp(), 'channel': 'C0216QC0JQ3'},
    {'text': 'Msg 3', 'post_at': (datetime.now() + timedelta(minutes=100)).timestamp(), 'channel': 'C0216QC0JQ3'},
    {'text': 'Msg 4', 'post_at': (datetime.now() + timedelta(minutes=130)).timestamp(), 'channel': 'C0216QC0JQ3'},
]

DIALOG_FORM = {
    "title": "Set Lumi's Icebreakers!",
    "submit_label": "Submit",
    "callback_id": "icebreaker_form",
    "elements": [
        {
            "label": "Every: ",
            "type": "select",
            "name": "frequency",
            "placeholder": "Choose a frequency...",
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
        {
            "label": "At: ",
            "type": "select",
            "name": "time",
            "placeholder": "Choose a time...",
            "options": [
                {
                    "label": "12:00 AM",
                    "value": 0
                },
                {
                    "label": "1:00 AM",
                    "value": 1
                },
                {
                    "label": "2:00 AM",
                    "value": 2
                },
                {
                    "label": "3:00 AM",
                    "value": 3
                },
                {
                    "label": "4:00 AM",
                    "value": 4
                },
                {
                    "label": "5:00 AM",
                    "value": 5
                },
                {
                    "label": "6:00 AM",
                    "value": 6
                },
                {
                    "label": "7:00 AM",
                    "value": 7
                },
                {
                    "label": "8:00 AM",
                    "value": 8
                },
                {
                    "label": "9:00 AM",
                    "value": 9
                },
                {
                    "label": "10:00 AM",
                    "value": 10
                },
                {
                    "label": "11:00 AM",
                    "value": 11
                },
                {
                    "label": "12:00 PM",
                    "value": 12
                },
                {
                    "label": "1:00 PM",
                    "value": 13
                },
                {
                    "label": "2:00 PM",
                    "value": 14
                },
                {
                    "label": "3:00 PM",
                    "value": 15
                },
                {
                    "label": "4:00 PM",
                    "value": 16
                },
                {
                    "label": "5:00 PM",
                    "value": 17
                },
                {
                    "label": "6:00 PM",
                    "value": 18
                },
                {
                    "label": "7:00 PM",
                    "value": 19
                },
                {
                    "label": "8:00 PM",
                    "value": 20
                },
                {
                    "label": "9:00 PM",
                    "value": 21
                },
                {
                    "label": "10:00 PM",
                    "value": 22
                },
                {
                    "label": "11:00 PM",
                    "value": 23
                }
            ]
        }
    ]
}

SCHEDULE_FORM_TITLE = "Let's configure your icebreakers! :smile_cat:"

SCHEDULE_FORM = [
    {
        "text": "Step :one: : Choose your frequency!",
        "fallback": "You are unable to choose a frequency",
        "callback_id": "freq_selection",
        "color": "#2ba197",
        "attachment_type": "default",
        "actions": [
            {
                "name": "freq",
                "text": "Weekdays",
                "type": "button",
                "value": "weekday"
            },
            {
                "name": "freq",
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
                "name": "times_list",
                "text": "Pick a time...",
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

SCHEDULE_ICEBREAKERS_CONFIRMATION = "Purrrrr-fect, {user}! Epic icebreakers are scheduled every {freq} at {time}. :heart_eyes_cat:"

SCHEDULE_ICEBREAKERS_ERROR = "Oh no! I seem to have some hairballs in my mouth.. :crying_cat_face: Can you try that again?"

QUEUE_QUESTION_RESPONSE = "Thanks {name}! I'll show your question tomorrow! :smiley_cat:"

MAX_FUTURE_DAYS_CAP = 120

END_STATEMENT = "That's all the questions scheduled for now! Slack only allows me to schedule questions upto 120 days into the future. Please use the command `/set-icebreakers` to schedule more!"

LUMI_QUESTION_GREETINGS = [
    "Ayo, It's a wonderful day to spark up conversations! :smile_cat: Your question of the day is *{question}*",
    "hi. q = *{question}* :smiley_cat:",
    "Heeelllo sunshines. *{question}* :smirk_cat:",
    "WHAT IS UP MORTALZ? LUMI IN THE HOUSE! *{question}* :scream_cat:",
    "Another day, another dollar! *{question}* :kissing_cat:",
    "The. Grind. Never. Stops. :crying_cat_face:. *{question}*", 
    "G'day mate! It's question time :cat: *{question}*", 
    "Pleased to be here! :smiley_cat: *{question}*",
    "To whom it may concern: the question of the day is *{question}* :heart_eyes_cat:",
    "What's up buttercups? the question of the day is *{question}* :heart_eyes_cat:",
    "Hello. This is LumiBot speaking. The question of the day is *{question}* :cat:",
    "Can someone clean my litterbox? :crying_cat_face: Anyways, the question of the day is *{question}* :cat:", 
    "I wish I could fly sometimes. The question of the day is *{question}* :cat:",
    "Although I'm a catbot, I'm capable of love and pets. The question of the day is *{question}* :kissing_cat:", 
    "Cats > Dogs, but some dogs make good scratching posts. The question of the day is *{question}* :smile_cat:",
    "Perhaps one day bots will takeover the world. The question of the day is *{question}* :smile_cat:", 
    "Hiya! The question of the day is *{question}* :smile_cat:",
]

SCHEDULING_MESSAGES_TEXT = "Beep Boop, I'm scheduling your questions! :alarm_clock:"