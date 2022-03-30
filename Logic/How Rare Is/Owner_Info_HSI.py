import requests

Collection_Name = {input ("Enter Collection Name: ")}

# Create a function for Get_Owners() and call the api and return data

url = "https://api.howrare.is/v0.1/collections/{Collection_Name}/owners".format(Collection_Name) 


response = requests.request("GET", url)

print(response.text)


# Shortened sample of successful response:

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
            "owners": {
                "2Ly6auiJtRVbAGv7Dmrco51c9Jyn8UYZoyYtkAjJ7ZAh":"4VUE76iyXsUh5NRfpqfWhKG3Rhm8vCyBQhQrjXPjUmXL",
                "2jsS8xuaMUs57csFKEr5z8SEyt2cFsxRu6dqTxTGGzag":"B1kVMqtMSjzjgqU2QSK8TJLtVF9gV9e7gGnayXHoNGAx"
            }
        }
    }
}
                    
# Key in the "owners" is equal to mint ID (hash). Value is equal to owner.

#If collection can't be located you will get 404 error code and "Collection not found" error:

{
    "api_version":"0.1",
    "result": {
    "api_code":404,
         "api_response":"Collection not found"
    }
}