from typing import Collection
import requests

Collection_Name = (input("Enter Collection Name: "))    
# Collection Slug Name to be swapped for this

def Retrieving_A_Single_Collection_OpenSea():

   import requests
   collection_slug_name = Collection_Name.lower().replace(" ", "-")

   # Get the data from the API (Retrieving a single collection) **Very Important** This is the one that would be used the most
   # collection_slug "The collection slug of this collection that is used to uniquely link to this collection on OpenSea"

   url = "https://api.opensea.io/api/v1/collection/collection_slug_name"

   headers = {"X-API-KEY": "__API_KEY__"}
   
   # '__API_KEY__' stands for the actual api key that you get from OpenSea

   response = requests.request("GET", url, headers=headers)

   print(response.text)

