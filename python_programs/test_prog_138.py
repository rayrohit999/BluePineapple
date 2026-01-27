import pytest
from prog_138 import checkRepresentation

@pytest.mark.parametrize("value", [0, -5])
def test_negative(value):
    with pytest.raises(ValueError):
        checkRepresentation(value)

def test_exception():
    with pytest.raises(TypeError):
        checkRepresentation("70")

def test_true():
    assert checkRepresentation(80)

def test_false():
    assert not checkRepresentation(71)
