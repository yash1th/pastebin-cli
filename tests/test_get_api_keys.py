import pytest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(sys.path[0]), 'pbin'))

from get_api_keys import get_dev_api_key, get_user_api_key

#testing for PASTEBIN_DEV_API_KEY
@pytest.fixture()
def export_dev_key():
    os.environ['PASTEBIN_DEV_API_KEY'] = '11111111111111111111111111111111'
    yield
    del os.environ['PASTEBIN_DEV_API_KEY']

@pytest.mark.usefixtures('export_dev_key')
class Test_dev_key():
    def test_dev_api_key_length(self):
        assert len(get_dev_api_key()) == 32

    def test_dev_api_key_type(self):
        assert type(get_dev_api_key()) == str

def test_no_dev_key():
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        get_dev_api_key()
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == -1


#testing for PASTEBIN_USER_API_KEY
@pytest.fixture()
def export_user_key():
    os.environ['PASTEBIN_USER_API_KEY'] = '11111111111111111111111111111111'
    yield
    del os.environ['PASTEBIN_USER_API_KEY']

@pytest.mark.usefixtures('export_user_key')
class Test_user_key():
    def test_user_api_key_length(self):
        assert len(get_user_api_key()) == 32

    def test_user_api_key_type(self):
        assert type(get_user_api_key()) == str

def test_no_user_key():
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        get_user_api_key()
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == -2