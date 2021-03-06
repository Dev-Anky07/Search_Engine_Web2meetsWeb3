## Read me file for Magic Eden ##

# ** Read all Documentation for Magic Eden  ** #

#  Classify Different Functions according to usage and needs for data calling  #

#*  Main Functions to focus on is retrieving Entire collection and collection stats  *

#   aka Metadata

#Then Classify Different functions and descibe them shortly in this readme file

# The included Functions are as follows :-

# # Get Collections {Get information of collections}
#* api-mainnet.magiceden.dev/v2/collections?offset=0&limit=200

import requests

url = "api-mainnet.magiceden.dev/v2/collections?offset=0&limit=3"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

# Get Specific Collections 
#* api-mainnet.magiceden.dev/v2/collections/:symbol/listings?offset=0&limit=20

import requests

url = "api-mainnet.magiceden.dev/v2/collections/btest/listings?offset=0&limit=20"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

# Get Collection stats {Get information of collection stats}
#* api-mainnet.magiceden.dev/v2/collections/:symbol/stats

import requests

url = "api-mainnet.magiceden.dev/v2/collections/runcible/stats"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

# Get Collection Activities {Get activities of a collection buy/sell/trade}
#* api-mainnet.magiceden.dev/v2/collections/:symbol/activities?offset=0&limit=100

import requests

url = "api-mainnet.magiceden.dev/v2/collections/runcible/activities?offset=0&limit=100"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

# Get launchpad Info
#* api-mainnet.magiceden.dev/v2/launchpad/collections?offset=0&limit=200

import requests

url = "api-mainnet.magiceden.dev/v2/launchpad/collections?offset=0&limit=200"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)