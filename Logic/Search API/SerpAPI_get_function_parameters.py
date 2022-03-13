# Rapid API get request **Manipulate Inputs here to get desired relults**

import json
import requests
# set up the request parameters
# create variables for all parameters
# replace the placeholder with your own data

params = {
  'api_key': '9F3022F9163D4D9389D6D1F4F64F3A30',# Replace with your own api key and its placeholder
  'q': 'Cool Cats',# Replace with your own search term
  'sort_by': 'relevance',# Replace with your own sort term
  'device': 'desktop',# Replace with your own device (desktop, mobile, tablet)
  'output': 'json', # Replace with your own output (Curl, PHP, Python, Node.js)) *json gives out the bussin links***
  'hl': 'en',# Replace with your own Google UI language
  'gl': 'in',# Replace with your country code
  'include_answer_box': 'true',# Replace with your own answer box (true, false)
  'time_period': 'last_year',# Replace with period (last_year, last_month, last_week, last_day)
  'location': 'Delhi,India',# Replace with your own Google Geolocation
  'google_domain': 'google.co.in',# Replace with your own Google Domain (google.com or google.co.in) 'in' representing your country of origin
  'page': '1',# Replace with your own page number (Defaults to 1)
  'filter': '1',# Replace with your own filter (Defaults to 1)
  'num': '5'#  Replace with your own number of results (Max is 100)
}

# make the http GET request to Scale SERP
api_result = requests.get('https://api.scaleserp.com/search', params)

# print the HTML response from Scale SERP
print(api_result.content)

# make the http GET request to Scale SERP
# api_result = requests.get('https://api.scaleserp.com/search', params)

# print the JSON response from Scale SERP
# print(json.dumps(api_result.json()))