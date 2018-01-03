import json, boto3, domovoi

app = domovoi.Domovoi()

# Use the following command to log a CloudWatch Logs message that will trigger this handler:
# python -c'import watchtower as w, logging as l; L=l.getLogger(); L.addHandler(w.CloudWatchLogHandler()); L.error(dict(x=8))'
# See http://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html for the filter pattern syntax
@app.cloudwatch_logs_sub_filter_handler(log_group_name="watchtower", filter_pattern="{$.x = 8}")
def monitor_cloudwatch_logs(event, context):
    print("Got a CWL subscription filter event:", event)

