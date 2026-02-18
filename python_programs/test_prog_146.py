import pytest
from prog_146 import total_ascii_value


def test_basic_string():
    assert total_ascii_value("ABC") == 198


def test_lowercase_string():
    assert total_ascii_value("abc") == 294


def test_mixed_characters():
    assert total_ascii_value("A1!") == ord("A") + ord("1") + ord("!")


def test_string_with_space():
    assert total_ascii_value("A B") == ord("A") + ord(" ") + ord("B")


def test_empty_string():
    assert total_ascii_value("") == 0


def test_numeric_string():
    assert total_ascii_value("123") == ord("1") + ord("2") + ord("3")


@pytest.mark.parametrize(
    "value",
    [
        123,
        None,
        ["A", "B"],
        {"a": 1},
        3.14,
    ]
)
def test_type_error(value):
    with pytest.raises(TypeError):
        total_ascii_value(value)
