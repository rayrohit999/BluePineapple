import pytest
from prog_140 import singleOccurrence

def test_basic_case():
    data = [(1, 2), (3, 4), (2, 3)]
    assert singleOccurrence(data) == [1, 4]

def test_all_unique():
    data = [(1, 2), (3, 4)]
    assert singleOccurrence(data) == [1, 2, 3, 4]

def test_no_single_occurrence():
    data = [(1, 2), (2, 1)]
    assert singleOccurrence(data) == []

def test_single_tuple():
    data = [(5, 6, 7)]
    assert singleOccurrence(data) == [5, 6, 7]

def test_empty_list():
    assert singleOccurrence([]) == []

@pytest.mark.parametrize("value", [None, "123", (1, 2), [1, 2, 3]])
def test_invalid_input_type(value):
    with pytest.raises(TypeError):
        singleOccurrence(value)

@pytest.mark.parametrize(
    "value",
    [
        [(1, 2), [3, 4]],
        [(1, 2), "34"],
        [(1, 2), 5],
    ]
)
def test_invalid_inner_element(value):
    with pytest.raises(TypeError):
        singleOccurrence(value)
