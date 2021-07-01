# https://realpython.com/pytest-python-testing/

import pytest
import requests

@pytest.fixture()
def data_of_people():
    return [{'first_name': 'chandra',
             'last_name': 'pandit',
             'position': 'engineer'},
            {'first_name': 'rohit',
             'last_name': 'singh',
             'position': 'manager'}
            ]

# Disable network calls
@pytest.fixture(autouse=True)
def disable_network_calls(monkeypatch):
    def set_error():
        raise RuntimeError("Networks calls are not allowed")
    monkeypatch.setattr(requests, 'get', lambda *args, **kwargs: set_error())


def data_for_display(data):
    res = []
    for item in data:
        res.append(item['first_name']+' '+item['last_name'] + ' ' + item['position'])
    return res

def data_for_excel(data):
    res = []
    for item in data:
        res.append(item['first_name'])
        res.append(item['last_name'])
        res.append(item['position'])
    return res

def test_for_display_data(data_of_people):
    assert data_for_display(data_of_people) == ['chandra pandit engineer', 'rohit singh manager']

@pytest.mark.skip
def test_for_excel_data(data_of_people):
    assert data_for_excel(data_of_people) == ['chandra', 'pandit', 'engineer', 'rohit', 'singh', 'manager']

@pytest.mark.xfail
def test_for_check_fail():
    assert False

# pytest -m network_calls -> to run marked test case
# pytest -m "not network_calls" -> to run all test case except marked one
# @pytest.mark.network_calls
# def test_api_calls():
#     res = requests.get("https://reqres.in/api/users?page=2")
#     assert res.status_code == 200


# ****************************** TEST PARAMETRIZATION ****************************
def is_palindrome(string):
    string = string.lower()
    new_string = ''
    for c in string:
        if ('a' <= c <= 'z') or ('A' <= c <= 'Z'):
            new_string += c
    l = 0
    h = len(new_string) - 1
    while l < h:
        if new_string[l] != new_string[h]:
            return False
        l += 1
        h -= 1
    return True

@pytest.mark.parametrize('palindrome', [
    "",
    "a",
    "boB",
    "Never odd or even",
    "Never odd or even?"]
)
def test_is_palindrome(palindrome):
    assert is_palindrome(palindrome)

@pytest.mark.parametrize('not_palindrome',['ab', 'abab'])
def test_is_not_palindrome(not_palindrome):
    assert not is_palindrome(not_palindrome)


@pytest.mark.parametrize('may_be_palindrome, expected_result', [
    ("boB", True),
    ("Never odd or even", True),
    ("abab", False)
])
def test_palindrome_combine(may_be_palindrome, expected_result):
    assert is_palindrome(may_be_palindrome) == expected_result
