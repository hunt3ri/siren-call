import os
import logging
import requests

from dotenv import load_dotenv


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def send_slack_message(project: str, status: str):
    """ Send message to slack"""
    web_hook = os.getenv("SLACK_WEB_HOOK", "NOT_SET")

    if web_hook == "NOT_SET":
        raise ValueError("Web Hook Env Var not set")

    # Send message to slack
    response = requests.post(
        web_hook,
        json={
            "text": f"Hey <!channel> Building project *{project}* status is *{status}* :smile:"
        },
    )

    print(response.status_code)


def parse_build_event(build_event: dict):
    """ Parse build event to extract notification details """
    status = build_event["detail"]["build-status"]
    project = build_event["detail"]["project-name"]
    logger.debug(f"Project: {project}")
    logger.debug(f"Status: {status}")
    return project, status


def send_message_handler(event: dict, context):
    """ Handle cloudwatch codebuild event"""
    logger.debug(f"CloudWatch event received: {event}")
    project, status = parse_build_event(event)
    send_slack_message(project, status)


if __name__ == "__main__":
    load_dotenv()
    print("Sending message")
    send_slack_message("TEST PROJECT", "TEST STATUS")
