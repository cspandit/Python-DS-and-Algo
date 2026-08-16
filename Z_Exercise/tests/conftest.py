import pytest
from pygments.lexer import default


@pytest.fixture()
def my_fixture():
    return 1


def pytest_addoption(parser):
    parser.addoption('--opt', action='store_true', help='test option')
    parser.addoption('--foo', action='store', default='bar', help='foo and bar')
