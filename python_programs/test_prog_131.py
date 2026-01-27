import pytest
from prog_131 import reverseVowel

def test_zero_vowel():
    assert reverseVowel("bcdfgh") == "bcdfgh"

def test_one_vowel():
    assert reverseVowel("cat") == "cat"

def test_odd_no_of_vowel():
    assert reverseVowel("roair") == "riaor"

def test_even_no_of_vowel():
    assert reverseVowel("rohan") == "rahon"

def test_TypeError():
    with pytest.raises(TypeError):
        reverseVowel(12343)