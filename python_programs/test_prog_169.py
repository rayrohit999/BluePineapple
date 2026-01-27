import pytest
from prog_169 import getPellNumber

@pytest.mark.parametrize("value", [0, -5])
def test_ValueError(value):
    with pytest.raises(ValueError):
        getPellNumber(value)

def test_base_cases():
    assert getPellNumber(1) == 1
    assert getPellNumber(2) == 2

@pytest.mark.parametrize(
    "n, expected",
    [
        (3, 5),
        (4, 12),
        (5, 29),
        (6, 70),
        (7, 169),
    ]
)
def test_known_values(n, expected):
    assert getPellNumber(n) == expected

def test_large_value():
    assert getPellNumber(10) == 2378

@pytest.mark.parametrize("value", ["10", None, [3], (4,), True])
def test_type_error(value):
    with pytest.raises(TypeError):
        getPellNumber(value)
