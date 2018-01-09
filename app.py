import os, json
import boto3, domovoi
from slackclient import SlackClient

app = domovoi.Domovoi()

slack_token = os.environ["SLACK_API_TOKEN"]
slack = SlackClient(slack_token)

@app.cloudwatch_logs_sub_filter_handler(log_group_name="/aws/lambda/jma-xml_atomfeed", filter_pattern='Error')
def monitor_cloudwatch_logs(event, context):
    toslack('jma-xml_atomfeed', event['logEvents'][0]['message'])



def toslack(name, message):
    slack.api_call(
        "chat.postMessage",
        channel="#error",
        text="[" + name + "] " + message
    )


