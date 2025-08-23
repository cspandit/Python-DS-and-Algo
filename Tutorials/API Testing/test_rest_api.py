import pytest
import requests
import json

@pytest.fixture()
def base_url():
    return "https://reqres.in/api/"

def test_get_api_data(base_url):
    url = base_url + "resource"
    headers = {'x-api-key': 'reqres-free-v1'}
    response = requests.get(url=url, headers=headers)
    assert response.status_code == 200
    response_data = response.json()
    response_data1 = json.loads(response.text)
    assert response_data  == response_data1
    assert response_data['total'] == 12


def test_get_api_users():
    url = "https://reqres.in/api/users"
    headers = {'x-api-key': 'reqres-free-v1'}
    response = requests.get(url=url, headers=headers)
    assert response.status_code == 200
    response_data = response.json()
    first_user = response_data['data'][0]['first_name']
    assert first_user == "George"

@pytest.mark.parametrize("username,email",[
    ("Chandra", "test@gmail.com"),
    ("Manisha", "test1@gmail.com")
])
def test_post_api_create_user_new(username, email):
    request_json = {
        "username": username,
        "email": email,
        "password": "chandu123"
    }
    headers = {
        'x-api-key': 'reqres-free-v1',
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }
    url = "https://reqres.in/api/register"
    response = requests.post(url=url, headers=headers, data=request_json)
    print(response.text)
    assert response.status_code == 400
    assert json.loads(response.text)['error'] == "Internal server error"

def test_put_api_update_user():
    url = "https://api.restful-api.dev/objects/"
    data = {
       "name": "Apple MacBook Pro 16",
       "data": {
          "year": 2019,
          "price": 2049.99,
          "CPU model": "Intel Core i9",
          "Hard disk size": "1 TB",
          "color": "silver"
            }
        }
    data = json.dumps(data)
    headers = {"content-type": "application/json"}
    response = requests.put(url=url, data=data, headers=headers)
    assert response.status_code == 200

@pytest.mark.skip
def test_post_api_create_user():
    request_json = {
        "username": "George",
        "email": "george.bluth@reqres.in",
        "password": "123"
    }
    headers = {
        'x-api-key': 'reqres-free-v1',
        'Content-Type': 'application/json'
    }
    url = "https://reqres.in/api/login"
    response = requests.post(url=url, headers=headers, params=request_json)
    print(response.text)
    assert response.status_code == 200
