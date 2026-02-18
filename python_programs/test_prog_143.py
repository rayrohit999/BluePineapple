import pytest
from prog_143 import countLists

def test_basic_case():
    data = (1, [2, 3], 4, [5])
    assert countLists(data) == 2

def test_no_lists():
    data = (1, 2, 3)
    assert countLists(data) == 0

def test_all_lists():
    data = ([1], [], [2, 3])
    assert countLists(data) == 3

def test_empty_tuple():
    assert countLists(()) == 0

def test_nested_structures():
    data = ([1, [2, 3]], (4, 5), {"a": 1}, [6])
    assert countLists(data) == 2

@pytest.mark.parametrize("value", [None, [], [1, 2], "123", 123])
def test_invalid_input(value):
    with pytest.raises(TypeError):
        countLists(value)