# importing libraries needed for the webhook
import requests
#initiating your webhook url
webhook_url='yourwebhookurl'
#message you want to send 
text='yourmessage'
# initiating the data you want to send
data = {
'event':'user_signed_up',
'user_id':12345,
'content':'text'
}
#making a function for sending information
def send(message,url):
#sending the data to your webhook
 requests.post(url, json=message)
send(data,webhook_url)