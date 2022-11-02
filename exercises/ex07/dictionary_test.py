"""EX07 - Dictionary Functions Tests."""

__author__ = "730489241"

from exercises.ex07.dictionary import invert, favorite_color, count
import pytest


def test_invert() -> None:
    """Tests 'invert' function."""
    fruit_color: dict[str, str] = {"Apple": "Red", "Orange": "Orange", "Grape": "Purple"}
    assert invert(fruit_color) == {"Red": "Apple", "Orange": "Orange", "Purple": "Grape"}


with pytest.raises(KeyError):
    """Test for KeyError"""
    my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
    invert(my_dictionary)


def test_edge_invert() -> None:
    """Tests 'invert' function with empty dict."""
    xs: dict[str, str] = {}
    assert invert(xs) == {}


def test_second_invert() -> None:
    """Tests 'invert' function a second time."""
    xs: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert invert(xs) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_favorite_color() -> None:
    """Tests favorite_color."""
    xs: dict[str, str] = {'Ray': 'purple', 'David': 'red', 'Sam': 'orange', 'Jack': 'orange'}
    assert favorite_color(xs) == 'orange'


def test_favorite_color_same() -> None:
    """Tests if favorite_color works with the same color."""
    xs: dict[str, str] = {'Ray': 'blue', 'David': 'blue', 'Sam': 'blue', 'Jack': 'blue'}
    assert favorite_color(xs) == 'blue'


def test_favorite_color_tie() -> None:
    """Tests if favorite_color works when there's a tie for best color."""
    ys: dict[str, str] = {'Ray': 'blue', 'David': 'blue', 'Sam': 'red', 'Jack': 'red'}
    assert favorite_color(ys) == 'blue'


def test_count_case_one() -> None:
    """Tests count function."""
    xs: list[str] = ["blue", "blue", "red", "blue", "red", "red"]
    assert count(xs) == {'blue': 3, 'red': 3}


def test_count_case_two() -> None:
    """Tests count again."""
    xs_one: list[str] = ["one"]
    xs_two: list[str] = ["two", "two"]
    xs_three: list[str] = ["three", "three", "three"]
    xs_four: list[str] = ["four", "four", "four", "four"]
    xs: list[str] = xs_one + xs_two + xs_three + xs_four
    assert count(xs) == {'one': 1, 'two': 2, 'three': 3, 'four': 4}


def test_count_edge_case() -> None:
    """Tests edge case."""
    xs: list[str] = list()
    i: int = 0
    while i < 10:
        xs.append("ten")
        i += 1
    i = 0
    while i < 20:
        xs.append("twenty")
        i += 1    
    i = 0
    while i < 7:
        xs.append("seven")
        i += 1    
    i = 0
    while i < 9:
        xs.append("nine")
        i += 1    
    i = 0
    while i < 6:
        xs.append("six")
        i += 1    
    assert count(xs) == {'ten': 10, 'twenty': 20, 'seven': 7, 'nine': 9, 'six': 6}