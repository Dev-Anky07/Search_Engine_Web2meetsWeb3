# # Get Collections {Get information of collections}
#* api-mainnet.magiceden.dev/v2/collections?offset=0&limit=200

import requests

url = "api-mainnet.magiceden.dev/v2/collections?offset=0&limit=3"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
