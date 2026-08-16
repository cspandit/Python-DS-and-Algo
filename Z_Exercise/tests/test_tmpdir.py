import pytest
import json

def test_tmpdir(tmpdir):
    file_a = tmpdir.join("file_a")
    dir_a = tmpdir.mkdir("dir_a")
    file_b = dir_a.join("file_b")

    file_a.write("This is file a")
    file_b.write("This is file b")

    assert file_a.read() == "This is file a"
    assert file_b.read() == "This is file b"


def test_tmpdir_factory(tmpdir_factory):
    dir_A = tmpdir_factory.mktemp('dir_A')
    dir_B = tmpdir_factory.mktemp('dir_B')
    file_A = dir_A.join('file_A')
    file_B = dir_B.join("file_B")

    file_A.write("This is file A")
    file_B.write("This is file B")

    assert file_A.read() == "This is file A"
    assert file_B.read() == "This is file B"


@pytest.fixture(scope='module')
def create_json_file(tmpdir_factory):
    json_file = tmpdir_factory.mktemp('test').join('test.json')
    data = {'name':'chandra', 'age': 21}
    with open(json_file, 'w') as f:
        json.dump(data, f)
    return json_file

def test_json_file_name(create_json_file):
    with open(create_json_file, 'r') as f:
        data = json.load(f)
    assert data['name'] == 'chandra'

def test_json_file_age(create_json_file):
    with open(create_json_file, 'r') as f:
        data = json.load(f)
    assert data['age'] == 21