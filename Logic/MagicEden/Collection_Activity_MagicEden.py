# Get Collection Activities {Get activities of a collection buy/sell/trade}
#* api-mainnet.magiceden.dev/v2/collections/:symbol/activities?offset=0&limit=100

import requests

# create a function Get_Activity() or Get_Collection_Activity() 

url = "api-mainnet.magiceden.dev/v2/collections/runcible/activities?offset=0&limit=100"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)