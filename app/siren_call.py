import os
import requests

from dotenv import load_dotenv


def send_message():
    web_hook = os.getenv("SLACK_WEB_HOOK", 'NOT_SET')

    if web_hook == 'NOT_SET':
        raise ValueError('Web Hook Env Var not set')

    # Send message to slack
    response = requests.post(web_hook, json={"text": "Hello, World!"})

    print(response.status_code)


def send_message_handler(event, context):
    # TODO handle lambda event
    send_message()


if __name__ == "__main__":
    load_dotenv()
    print('Sending message')
    send_message()
