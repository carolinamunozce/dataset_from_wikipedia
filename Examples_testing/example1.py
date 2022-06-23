import pytest
from function2 import suma

def test_fx():
    assert type(suma(1,4)) == int


test_fx()