# AWS Lambda Webhook Endpoint for Whanpia - Call & Message Alert Service

- This repo contains Python lambda function for playing call audio in [whanpia-alerts](https://github.com/nedd-ludd/whanpia-alerts/).

- Please refer to the full project [README.md](https://github.com/nedd-ludd/whanpia-alerts/blob/main/README.md)

## Code Explaination

- Lambda function is triggered by AWS API gateway endpoint receving request(s) from Telnyx.
- Various event types are recieved like "call.initiated" although code logic will run on "call.answered".

- A "call_control_id" is contained within the request and the specific Telnyx call object can be retrieved.
- The object is then passed link to audio in S3 bucket to play to recipient.

- The code relies on the telnyx package which can be found in [whanpia-lambda-layers](https://github.com/nedd-ludd/whanpia-alerts-layers)

- In order to upload as an AWS Lambda Function, the code must be compressed as a .zip file prior to uploading.
