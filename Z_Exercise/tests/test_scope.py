import pytest
@pytest.fixture(scope='function')
def func_scope():
    pass

@pytest.fixture(scope='session')
def sess_scope():
    pass

@pytest.fixture(scope='module')
def mod_scope():
    pass

@pytest.fixture(scope='class')
def class_scope():
    pass

def test_one(sess_scope, mod_scope, func_scope):
    pass
def test_two(sess_scope, mod_scope, func_scope):
    pass

@pytest.mark.usefixtures('class_scope')
class TestSomething:
    def test_three(self):
        pass
    def test_four(self):
        pass