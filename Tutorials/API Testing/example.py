import requests
import json
import jsonpath

# Get Request
url = "https://reqres.in/api/users?page=2"
headers = {}
headers['x-api-key'] = 'reqres_d5ca6d1bc208462fa9ba94c2e5e585b7'
response = requests.get(url, headers=headers)
print(response)
print(response.content)# this will give raw string format
print(response.status_code)

# parsing in json format
json_response = json.loads(response.text)  # response.text give string format which is dumps in json format
print(json_response)

# Fetching value
data = jsonpath.jsonpath(json_response, 'data')  # jsonpath always return list object
print(data)  # so this will be list of list as data contain multiple dict value

data = json_response['data']  # this will contain list of dict value
print(data)

# Post request
url_post = "https://reqres.in/api/users"
# Read json input file and loads

with open('create_user.json', 'r') as file:
    input_json = file.read()
request_json = json.loads(input_json)
headers = {}
headers['x-api-key'] = 'reqres_d5ca6d1bc208462fa9ba94c2e5e585b7'
# make post request with request body/json
response = requests.post(url=url, data=request_json, headers=headers)
print(response.status_code)
print(response.content)




