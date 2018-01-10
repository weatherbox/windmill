import os, json
import domovoi
from slackclient import SlackClient

app = domovoi.Domovoi()

slack_token = os.environ["SLACK_API_TOKEN"]
slack = SlackClient(slack_token)

for func in ["jma-xml_atomfeed", "grib2tiles_download_msm", "grib2tiles_msm", "grib2tiles_tile-json-msm", "amedas_scrape-geojson"]:
    @app.cloudwatch_logs_sub_filter_handler(log_group_name="/aws/lambda/" + func, filter_pattern='Error')
    def monitor_cloudwatch_logs(event, context):
        toslack(event['logGroup'][12:], event['logEvents'][0]['message'])



def toslack(name, message):
    slack.api_call(
        "chat.postMessage",
        channel="#error",
        text="[" + name + "] " + message
    )


