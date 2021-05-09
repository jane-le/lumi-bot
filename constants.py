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

SCHEDULE_ICEBREAKERS_CONFIRMATION = "Purrrrr-fect! Your icebreakers are scheduled :heart_eyes_cat:"

QUEUE_QUESTION_RESPONSE = "Thanks {name}! I'll add it to the queue :smiley_cat:"