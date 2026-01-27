import pytest
from prog_137 import getZeroesRatio

def test_empty_list():
    with pytest.raises(Exception):
        getZeroesRatio([])

def test_Exception():
    with pytest.raises(TypeError):
        numList = (1, 2, 4, 12, 21, 0, 0, 34, 0)
        getZeroesRatio(numList)

def test_zeroes():
    numList = [1, 2, 4, 12, 21, 0, 0, 34, 0]
    assert getZeroesRatio(numList) == 3/len(numList)

def test_zero_zeroes():
    numList = [1, 2, 4, 12, 21, 98, 23, 34, 25]
    assert getZeroesRatio(numList) == 0

def test_all_zeroes():
    numList = [0, 0, 0, 0]
    assert getZeroesRatio(numList) == 1