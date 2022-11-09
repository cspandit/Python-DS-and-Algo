import pytest

@pytest.fixture 
def fixture_fun():
	return 1 

def test_my_fixture(fixture_fun):
	assert fixture_fun == 1

