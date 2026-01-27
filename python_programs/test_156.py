import pytest
from prog_156 import convert_string_tuple_to_integer

def test_basic_conversion():
    assert convert_string_tuple_to_integer(("1", "2")) == (1, 2)

def test_single_element():
    assert convert_string_tuple_to_integer(("10",)) == (10,)

def test_empty_tuple():
    with pytest.raises(TypeError):
        convert_string_tuple_to_integer(())

def test_large_numbers():
    assert convert_string_tuple_to_integer(("1000", "2000")) == (1000, 2000)
