# Rarity API
# Once you have retrieved list of collections you can look up rank for a specific collection. 
# To do that use "url" parameter from Collections API response to construct Rarity API url.
# Rarity URL is in the form of https://api.howrare.is/v0.1/collections/{collection} . 
# To retrieve Rarity data for SolanaMonkeyBusiness:
# GET https://api.howrare.is/v0.1/collections/smb

import requests

Collection_Name = {input ("Enter Collection Name: ")}

# Create a function for Get_Rarity() and call the api and return data

url = "https://api.howrare.is/v0.1/collections/{Collection_Name}".format(Collection_Name) 

#check what format collection name does

response = requests.request("GET", url)

print(response.text)

## Results

# If a properly formatted request you will get Rarity data (items trimmed to 1 item to save space here):

{
    "api_version":"0.1",
    "result": {
        "api_code":200,
        "api_response":"Success",
        "data": {
            "collection":"SolanaMonkeyBusiness (SMB)",
            "ranking_url":"https://howrare.is/smb",
            "twitter":"https://twitter.com/SolanaMBS",
            "discord":"http://discord.gg/solanamonkey",
            "website":"http://solanamonkey.business",
            "description":"5000 Solana inspired generative NFTs",
            "logo":"https://media.howrare.is/images/project_logo/smb.jpg",
            "items": [
                {
                    "id":"1355",
                    "mint":"9ARngHhVaCtH5JFieRdSS5Y8cdZk2TMF4tfGSWFB9iSK",
                    "link":"https://howrare.is/smb/1355/",
                    "name":"SMB #1355",
                    "description":"SMB is a collection of 5000 randomly generated 24x24 pixels NFTs on the Solana Blockchain. Each SolanaMonkey is unique and comes with different type and attributes varying in rarity.",
                    "image":"https://arweave.net/wGChHSDTXTP9oAtTaYh9s8j1MRE0IPmYtH5greqWwZ4",
                    "attributes": [
                        {"name":"Attribute count", "value":2, "rarity":"45.96"},
                        {"name":"Type","value":"Skeleton","rarity":"2.42"},
                        {"name":"Clothes","value":"Orange Jacket","rarity":"1.04"},
                        {"name":"Ears","value":"None","rarity":"78.08"},
                        {"name":"Mouth","value":"None","rarity":"73.64"},
                        {"name":"Eyes","value":"None","rarity":"71.52"},
                        {"name":"Hat","value":"Crown","rarity":"0.02"}
                    ],
                    "rank":1,
                    "rank_algo":"howrare.is",
                    "all_ranks":
                    {
                        "howrare.is":1,
                        "trait_normalized":1
                    }
                }
            ]
        }
    }
}
 

# If collection will not be located you will get 404 error code and "Collection not found" error:

{
    "api_version":"0.1",
    "result": {
        "api_code":404,
        "api_response":"Collection not found"
    }
}

