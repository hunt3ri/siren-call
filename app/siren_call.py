import os
import logging
import requests

from dotenv import load_dotenv


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def send_message():
    web_hook = os.getenv("SLACK_WEB_HOOK", "NOT_SET")

    if web_hook == "NOT_SET":
        raise ValueError("Web Hook Env Var not set")

    # Send message to slack
    response = requests.post(web_hook, json={"text": "Hello, World 4!"})

    print(response.status_code)


def send_message_handler(event, context):
    # TODO handle lambda event
    logger.debug("Hi Iain, test logging")
    logger.debug(event)
    logger.debug(context)
    send_message()


if __name__ == "__main__":
    load_dotenv()
    print("Sending message")
    send_message()
