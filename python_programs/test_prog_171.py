import pytest
from prog_171 import getPerimeterPentagon

def test_TypeError():
    with pytest.raises(TypeError):
        getPerimeterPentagon("45")

def test_Exception():
    with pytest.raises(Exception):
        getPerimeterPentagon(23, 24)

# Regular Pentagon
def test_integer():
    assert getPerimeterPentagon(5) == 25

def test_float():
    assert getPerimeterPentagon(5.5) == 5.5 * 5

# Iregular Pentagon
def test_all_side():
    assert getPerimeterPentagon(5.5, 2, 3.5, 4, 8.8) == 23.8