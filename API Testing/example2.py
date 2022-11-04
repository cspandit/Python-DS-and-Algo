import requests
import json

url_post = "https://reqres.in/api/users"
req_body = {"name": "chandra", "job": "jobless"}
req_json = json.dumps(req_body)

res = requests.post(url_post, req_json)
print(res.content)