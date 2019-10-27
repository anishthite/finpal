import requests



# send sems
POST 

Content-Type: application/json
Autorization: Bearer <accessToken>


requests.post('https://oauth-cpaas.att.com/cpaas/smsmessaging/v1/0f0b7f62-7442-485f-beee-959dbf5b7c43/outbound/+12039099118/requests', data={})





{
    "outboundSMSMessageRequest": {
        "address": [
            "+16131234567"
        ],
        "clientCorrelator": "fc747ecf-c403-4cee-8327-80b38f311db9",
        "outboundSMSTextMessage": {
            "message": "hi :)"
        }
    }
}
