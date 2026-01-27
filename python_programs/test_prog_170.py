import pytest
from prog_170 import rangeSum

def test_basic_range_sum():
    assert rangeSum([1, 2, 3, 4, 5], 1, 3) == 9

def test_single_element():
    assert rangeSum([10, 20, 30], 1, 1) == 20

def test_full_list():
    assert rangeSum([1, 2, 3], 0, 2) == 6

def test_float_values():
    assert rangeSum([1.5, 2.5, 3.0], 0, 2) == 7.0

@pytest.mark.parametrize(
    "numbers, start, end",
    [
        ("123", 0, 1),
        (None, 0, 1),
        ([1, 2, "3"], 0, 2),
        ([1, 2, 3], 1.5, 2),
        ([1, 2, 3], 1, True),
    ]
)
def test_type_error(numbers, start, end):
    with pytest.raises(TypeError):
        rangeSum(numbers, start, end)

@pytest.mark.parametrize(
    "numbers, start, end",
    [
        ([1, 2, 3], -1, 2),
        ([1, 2, 3], 0, 5),
        ([1, 2, 3], 2, 1),
        ([], 0, 0),
    ]
)
def test_value_error(numbers, start, end):
    with pytest.raises(ValueError):
        rangeSum(numbers, start, end)

def test_zero_sum():
    assert rangeSum([0, 0, 0], 0, 2) == 0

def test_negative_numbers():
    assert rangeSum([-1, -2, -3], 0, 2) == -6