import pytest
from prog_168 import getFrequency

def test_basic_frequency():
    assert getFrequency([1, 2, 3, 2, 2, 4], 2) == 3

def test_single_occurrence():
    assert getFrequency([5, 6, 7], 6) == 1

def test_value_not_present():
    assert getFrequency([1, 2, 3], 4) == 0

def test_float_frequency():
    assert getFrequency([1.1, 2.2, 1.1, 3.3], 1.1) == 2

def test_empty_list():
    assert getFrequency([], 5) == 0

def test_all_same_elements():
    assert getFrequency([3, 3, 3, 3], 3) == 4

@pytest.mark.parametrize("arr", [None, "123", 123, (1, 2, 3)])
def test_invalid_array_type(arr):
    with pytest.raises(TypeError):
        getFrequency(arr, 2)

@pytest.mark.parametrize("value", ["2", None, True, [2]])
def test_invalid_value_type(value):
    with pytest.raises(TypeError):
        getFrequency([1, 2, 3], value)

@pytest.mark.parametrize("arr", [[1, 2, "3"], [1, None, 3], [True, 2, 3]])
def test_invalid_list_elements(arr):
    with pytest.raises(TypeError):
        getFrequency(arr, 2)
