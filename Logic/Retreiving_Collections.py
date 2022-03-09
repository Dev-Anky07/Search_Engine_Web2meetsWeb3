import requests

# Implement functionality to input '__Wallet_Adress_Other_Assets__' and 'X-API-KEY'
# maybe importing api key wouldnt be required as it would be asked in the main program and this variable would inherit that

# Get the data from the API (Retreiving Collections)

# Wallet Holder's other Assets is asset_owner && offset and limit are self explainatory

url = "https://api.opensea.io/api/v1/collections?asset_owner=__Wallet_Adress_Other_Assets__&offset=0&limit=300"

headers = {
    "Accept": "application/json",
    "X-API-KEY": ""
}

# Implement functionality to call this function'Retreiving_Collections'