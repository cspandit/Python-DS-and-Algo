import pytest
import monkey_function_demo


@pytest.fixture()
def mock_get_user_name(monkeypatch):
    def mock_get_user_name():
        return ("John Doe")
    monkeypatch.setattr("monkey_function_demo.get_user_name", mock_get_user_name)

def test_greet_user(mock_get_user_name):
    assert monkey_function_demo.greet_user() == "Hello John Doe"