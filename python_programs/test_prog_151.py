import pytest
from prog_151 import isCoprime

def test_basic_coprime():
    assert isCoprime(8, 15) is True


def test_not_coprime():
    assert isCoprime(6, 9) is False


def test_with_one():
    assert isCoprime(1, 99) is True


def test_same_numbers():
    assert isCoprime(7, 7) is False


def test_zero_and_one():
    assert isCoprime(0, 1) is True


def test_zero_and_number():
    assert isCoprime(0, 5) is False


@pytest.mark.parametrize(
    "a, b",
    [
        ("10", 5),
        (10, "5"),
        (None, 5),
        (5, None),
        (3.5, 2),
        (3, True),
    ]
)
def test_type_error(a, b):
    with pytest.raises(TypeError):
        isCoprime(a, b)


@pytest.mark.parametrize(
    "a, b",
    [
        (-3, 5),
        (3, -5),
        (-3, -5),
    ]
)
def test_value_error(a, b):
    with pytest.raises(ValueError):
        isCoprime(a, b)