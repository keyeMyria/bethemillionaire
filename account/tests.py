
import socket
import simplejson
import requests


campaign_id = '6rwSE'
api_key = '75a678181ff9476176fee468f8ef587a'
email = 'amirmubarak19@gmail.com'

ipaddress = socket.gethostbyname(socket.gethostname())

c = {
        'campaignId': campaign_id,
    }

data = {
    'name': 'mubarak',
    'email': email,
    'campaign': c,
    'ipAddress': ipaddress,
}

data_json = simplejson.dumps(data)

api_format = 'api-key %s' %api_key

headers = {
    'Content-Type': 'application/json',
    'X-Auth-Token': api_format,
}

r = requests.post('https://api.getresponse.com/v3/contacts', headers=headers, data=data_json)


print(r)
