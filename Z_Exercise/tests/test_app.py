import pytest
from app import divide, is_palindrome

@pytest.fixture(params=['aba', 'chandra', 'malayalam'])
def parametrized_fixture(request):
    return request.param

def test_parameterized_fixture(parametrized_fixture):
    assert is_palindrome(parametrized_fixture)

def test_divide_error():
    with pytest.raises(ZeroDivisionError) as error_info:
        divide(12, 0)
    error_msg = error_info.value.args[0]
    assert error_msg == 'Zero cannot divide anything'
@pytest.mark.skip(reason='Wrong case')
def test_divide_ok():
    assert divide(12,3) == 5

def test_divide_float():
    assert divide(12.0,3.0) == 4.0

@pytest.mark.parametrize('palindrome', [
    'aaa',
    'aba',
    'malayalam'
])
def test_is_palindrome(palindrome):
    assert is_palindrome(palindrome)

@pytest.mark.parametrize('maybe_palin, expected_result',[
    ('ab', False),
    ('aba', True)
])
def test_maybe_palindrome(maybe_palin, expected_result):
    assert is_palindrome(maybe_palin) == expected_result