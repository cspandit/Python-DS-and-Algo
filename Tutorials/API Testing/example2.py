import requests
import json
from requests.auth import HTTPBasicAuth

url_post = "https://reqres.in/api/users"
req_body = {"name": "chandra", "job": "jobless"}
req_json = json.dumps(req_body)

res = requests.post(url_post, req_json)
print(res.content)




# Making a get request
response = requests.get('https://api.github.com / user, ',
                        auth=HTTPBasicAuth('user', 'pass'))

# print request object
print(response)

# >>> import requests
# >>> from requests_oauthlib import OAuth1
#
# >>> url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
# >>> auth = OAuth1('YOUR_APP_KEY', 'YOUR_APP_SECRET',
# ...               'USER_OAUTH_TOKEN', 'USER_OAUTH_TOKEN_SECRET')
#
# >>> requests.get(url, auth=auth)

# from requests_oauthlib import OAuth1Session
# test = OAuth1Session('consumer_key',
#                     client_secret='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
# url = 'https://one-legged-ouath.example.com/username/test'
# r = test.get(url)
# print r.content