import pytest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(sys.path[0]), 'pbin'))

from get_api_key import get_api_key 

def test_api_key_length():
    assert len(get_api_key()) == 32

def test_api_key_type():
    assert type(get_api_key()) == str
