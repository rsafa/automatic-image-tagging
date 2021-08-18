import requests

api_key = 'API KEY'
api_secret = 'API SECRET'

image_url = 'THE IMAGE URL'

params = (('image_url', image_url),)
response = requests.get('https://api.imagga.com/v2/tags', params=params, auth=(api_key, api_secret))

list = response.json()

for i in list['result']['tags']:
        print(i['tag']['en'], ':', i['confidence'])