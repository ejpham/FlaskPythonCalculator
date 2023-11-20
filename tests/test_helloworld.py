import pytest
from src.helloworld import hello_world_return, hello_world_print

def test_hello_world_return():
    assert hello_world_return() == "Hello World!"

def test_hello_world_print(capfd):
    hello_world_print()
    out, err = capfd.readouterr()
    assert out == "Hello World!\n"
