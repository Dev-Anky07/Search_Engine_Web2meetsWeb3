import requests

# Create a seperate Get function for every retrieving usecase
# Try and get api key from opensea
# def get_api_key():
#    api_key = "YOUR_API_KEY"    Replace with your own api key and its placeholder
#    return api_key


# Get the data from the API (Retreiving Collections)
# Wallet Holder's other Assets is asset_owner && offset and limit are self explainatory

url = "https://api.opensea.io/api/v1/collections?asset_owner=__Wallet_Adress_Other_Assets__&offset=0&limit=300"

headers = {
    "Accept": "application/json",
    "X-API-KEY": ""
}

response = requests.request("GET", url, headers=headers)

print(response.text)

# Get the data from the API (Retreiving a Single Asset)
# ap1/v1/asset/asset_contract_address/token_id

url = "https://api.opensea.io/api/v1/assetasset_contract_address/token_id/?account_address=__check__&include_orders=true"

response = requests.request("GET", url)

print(response.text)

# Get the data from the API (Retrieving listings for an asset)

url = "https://api.opensea.io/api/v1/asset/asset_contract_address/token_id/listings?limit=20"

headers = {
    "Accept": "application/json",
    "X-API-KEY": "__API_KEY__"
}

response = requests.request("GET", url, headers=headers)

print(response.text)

# Get the data from the API (Retrieving offers for an asset)

url = "https://api.opensea.io/api/v1/asset/asset_contract_address/token_id/offers?limit=20"

headers = {
    "Accept": "application/json",
    "X-API-KEY": "__API_KEY__"
}

response = requests.request("GET", url, headers=headers)

print(response.text)

# Get the data from the API (Retrieving a single contract)

url = "https://api.opensea.io/api/v1/asset_contract/asset_contract_address"

headers = {"X-API-KEY": "__API_KEY__"}

response = requests.request("GET", url, headers=headers)

print(response.text)

# Get the data from the API (Retrieving a single collection) **Very Important** This is the one that would be used the most
#collection_slug "The collection slug of this collection that is used to uniquely link to this collection on OpenSea"

url = "https://api.opensea.io/api/v1/collection/collection_slug_name"

headers = {"X-API-KEY": "__API_KEY__"}

response = requests.request("GET", url, headers=headers)

print(response.text)

# Get the data from the API (Retrieving collection stats)

url = "https://api.opensea.io/api/v1/collection/collection_slug_name/stats"

headers = {
    "Accept": "application/json",
    "X-API-KEY": "__API_KEY__"
}

response = requests.request("GET", url, headers=headers)

print(response.text)

# Get the data from the API (Retrieving assets)
url = "https://api.opensea.io/api/v1/assets?owner=__owner_adress__&owner=__owner_adress__&token_ids=__token_ids__&collection=__exact_col_slug__&collection_slug=__collection_slug__&collection_editor=__collection_editor__&order_by=sale_price&order_direction=desc&asset_contract_address=__asset_contract_address__&limit=20&include_orders=true"

headers = {
    "Accept": "application/json",
    "X-API-KEY": "__API_KEY__"
}

response = requests.request("GET", url, headers=headers)

print(response.text)
