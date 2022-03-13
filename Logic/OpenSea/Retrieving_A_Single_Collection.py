import requests

collection_slug_name = input("Enter Collection Name: ")

# Get the data from the API (Retrieving a single collection) **Very Important** This is the one that would be used the most
# collection_slug "The collection slug of this collection that is used to uniquely link to this collection on OpenSea"

url = "https://api.opensea.io/api/v1/collection/collection_slug_name"

headers = {"X-API-KEY": "__API_KEY__"}

response = requests.request("GET", url, headers=headers)

print(response.text)

