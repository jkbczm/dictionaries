# importing libraries needed for the webhook
import requests
#initiating your webhook url
webhook_url='https://discord.com/api/webhooks/1365738814555033610/XsbRbh2vBVB0ke_HyayJsZG4SVHS6HPQQ4deAuivE0SzF8zXZeE2RA1E7YoyKWgL88iQ'
#message you want to send 
text= str(input("your message"))
# initiating the data you want to send
data = {
'content': text
}
#making a function for sending information
def send(message,url):
#sending the data to your webhook
 requests.post(url, json=message)
send(data,webhook_url)