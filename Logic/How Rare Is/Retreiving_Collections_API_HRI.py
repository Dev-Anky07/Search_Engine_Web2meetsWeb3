import requests

# Create a function for Get_collections() or Get_Collections_HSI() to call the api

url = "https://api.howrare.is/v0.1/collections" 

#check what format collection name does

response = requests.request("GET", url)

print(response.text)

# Shortened sample of successful response: showing only 2 collections

{
    "api_version": "0.1",
    "result": {
        "api_code": 200,
        "api_response": "Success",
        "data": [
            {
                "name": "SolanaMonkeyBusiness (SMB)",
                "url": "/smb",
                "logo": "https://media.howrare.is/images/project_logo/smb.jpg"
            },
            {
                "name": "Aurory",
                "url": "/aurory",
                "logo": "https://media.howrare.is/images/project_logo/aurory.jpg"
            }
        ]
    }
}