import requests

# Get the data from the API (Retreiving a Single Asset)
# ap1/v1/asset/asset_contract_address/token_id 
#Where Token Id = token_id  and Contract address of asset = asset_contract_address

url = "https://api.opensea.io/api/v1/asset/asset_contract_address/token_id/?account_address=__check__&include_orders=true"

response = requests.request("GET", url)

print(response.text)

# Implement functionality to return the data to the main program (Retrieving listings for an asset)