import pytest

from server import *

def test_server_address():
    assert get_server_address() == '127.0.0.1'

def test_server_port():
    assert get_server_port() == 8080
