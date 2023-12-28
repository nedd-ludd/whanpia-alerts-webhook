import json
import telnyx
import os


def lambda_handler(event, context):
    telnyx.api_key = os.environ.get('TEL_API_KEY')

    event_type = event["data"]["event_type"]

    if event_type == "call.answered":
        print(type(event))
        call_id = event["data"]["payload"]["call_control_id"]
        call = telnyx.Call.retrieve(call_id)
        # Call has been answered
        audio_url = "https://snoop-alert.s3.amazonaws.com/snoop.mp3"
        call.playback_start(audio_url=audio_url)

    return {
        'statusCode': 200,
        'body': json.dumps('Success!')
    }
