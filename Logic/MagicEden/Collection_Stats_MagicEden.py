# Get Collection stats {Get information of collection stats}
#* api-mainnet.magiceden.dev/v2/collections/:symbol/stats

import requests

# Create a function Get_Collection_Stats() and call when necessary

url = "api-mainnet.magiceden.dev/v2/collections/runcible/stats"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)