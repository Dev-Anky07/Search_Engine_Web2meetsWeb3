# Get Specific Collections 
#* api-mainnet.magiceden.dev/v2/collections/:symbol/listings?offset=0&limit=20

# Create a function Get_Collection() and call the api and return data and create Get_Collection_Stats() 

import requests

url = "api-mainnet.magiceden.dev/v2/collections/btest/listings?offset=0&limit=20"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)