import pytest
from src.arithmetic import *

def test_add():
    assert add(1, 2) == 3

def test_subtract():
    assert subtract(1, 2) == -1

def test_multiply():
    assert multiply(2, 3) == 6

def test_divide():
    assert divide(6, 3) == 2
