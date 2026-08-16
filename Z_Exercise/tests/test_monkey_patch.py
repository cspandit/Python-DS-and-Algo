import pytest
import app

@pytest.fixture()
def test_monkey(monkeypatch):
    def new_return_user():
        print("This is mocked function")
        return 'John Don'
    monkeypatch.setattr('app.return_user', new_return_user)


def test_return_user(test_monkey):
    assert app.return_user() == 'John Don'


def test_monkey_patch_env(monkeypatch, tmpdir):
    monkeypatch.setenv('HOME', str(tmpdir.mkdir('home')))
    app.write_to_home()
    data = app.read_from_home()
    print('data: {}'.format(data))
    assert data['name'] == 'chandra'