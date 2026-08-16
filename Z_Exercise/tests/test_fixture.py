import pytest

@pytest.fixture(name='bnf')
def big_fixture_name():
    """Big fixture function name can be renamed with name parameter"""
    return 2

def test_my_fixture(my_fixture):
    assert 1 == my_fixture

def test_my_fixture_negative(bnf):
    assert 2 == bnf