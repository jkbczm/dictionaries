# importing libraries needed for the webhook
import requests
#initiating your webhook url
webhook_url='yourwebhookurl'
#message you want to send 
message ='yourmessage'
# initiating the data you want to send
data = {
'event':'user_signed_up',
'user_id':12345,
'content':'message'
}
#sending the data to your webhook
requests.post(webhook_url, json=data)