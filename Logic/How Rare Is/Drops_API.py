# GET https://api.howrare.is/v0.1/drops

# All upcoming drops for Solana would be listed here and we'll have to parse it.

import requests

# add a function Get_Drops() here to call the api and return data

# Make seperate functions for all api's ar make one and use if else logic
# Get_Drops() v/s Get_Drops_HRI()

url = "https://api.howrare.is/v0.1/drops"

response = requests.request("GET", url)

print(response.text)