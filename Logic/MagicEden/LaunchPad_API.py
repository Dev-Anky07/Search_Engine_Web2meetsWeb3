# Get launchpad Info
#* api-mainnet.magiceden.dev/v2/launchpad/collections?offset=0&limit=200

import requests

# create a function Get_Launchpad_Info() or Get_Launchpad() and call when necessary

url = "api-mainnet.magiceden.dev/v2/launchpad/collections?offset=0&limit=200"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)