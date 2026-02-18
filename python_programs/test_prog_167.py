import pytest
from prog_167 import smallestPowerOf2

def test_exact_power_of_two():
    assert smallestPowerOf2(1) == 1
    assert smallestPowerOf2(2) == 2
    assert smallestPowerOf2(8) == 8
    assert smallestPowerOf2(32) == 32

def test_between_powers_of_two():
    assert smallestPowerOf2(3) == 4
    assert smallestPowerOf2(5) == 8
    assert smallestPowerOf2(17) == 32
    assert smallestPowerOf2(31) == 32

def test_edge_cases():
    assert smallestPowerOf2(1) == 1
    assert smallestPowerOf2(1023) == 1024

@pytest.mark.parametrize("value", [0, -1, -10])
def test_value_error(value):
    with pytest.raises(ValueError):
        smallestPowerOf2(value)

@pytest.mark.parametrize("value", [1.5, "10", None, [5], True])
def test_type_error(value):
    with pytest.raises(TypeError):
        smallestPowerOf2(value)
