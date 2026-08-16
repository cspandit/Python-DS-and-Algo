import time
import pytest

@pytest.fixture(scope='function', autouse=True)
def test_duration():
    start = time.time()
    yield
    stop = time.time()
    print('\nTest Duration: {:.2f}'.format(stop-start))

@pytest.fixture(scope='session', autouse=True)
def session_end():
    yield
    print('--')
    print('Session finished: {}'.format(time.strftime('%Y %m %d - %H:%M:%S', time.localtime(time.time()))))

def test_one():
    time.sleep(2)
def test_two():
    time.sleep(3)