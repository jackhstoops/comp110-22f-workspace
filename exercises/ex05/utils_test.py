"""EX05 - Utils Test."""

__author__ = "730489241"

from exercises.ex05.utils import only_evens
from exercises.ex05.utils import sub
from exercises.ex05.utils import concat


def test_only_evens() -> None:
    """Testing Only Evens."""
    xs: list[int] = [0, 1, 2, 4, 4, 2]
    assert only_evens(xs) == [2, 4, 4, 2]


def test_only_evens_no_evens() -> None:
    """Testing Only Evens with No Evens."""
    xs: list[int] = [1, 3, 5]
    assert only_evens(xs) == []


def test_only_evens_extreme() -> None:
    """Testing Only Evens with extreme values."""
    xs: list[int] = [1765678**2, 987656789, 765434567]
    assert only_evens(xs) == [1765678**2]


def test_concat() -> None:
    """Testing Concat with regular numbers."""
    one_xs: list[int] = [1, 2, 2, 3, 3]
    two_xs: list[int] = [3, 3, 2, 2, 1]
    assert concat(one_xs, two_xs) == [1, 2, 2, 3, 3, 3, 3, 2, 2, 1]


def test_concat_one_list() -> None:
    """Testing Concat with just one list."""
    one_xs: list[int] = []
    two_xs: list[int] = [3, 3, 2, 2, 1]
    assert concat(one_xs, two_xs) == [3, 3, 2, 2, 1]


def test_concat_extreme() -> None:
    """Testing Concat with extreme values."""
    one_xs: list[int] = [3**3, 6**2, 5**2]
    two_xs: list[int] = [10**100, 5**45]
    assert concat(one_xs, two_xs) == [27, 36, 25, 10**100, 5**45]


def test_sub() -> None:
    """Testing Sub. Regular."""
    xs: list[int] = [10, 20, 30, 40, 50]
    s_index: int = 2
    e_index: int = 4
    assert sub(xs, s_index, e_index) == [30, 40]


def test_sub_negative_start() -> None:
    """Testing Sub. with Starting Index Value Less Than 0."""
    xs: list[int] = [10, 20, 30, 40, 50]
    s_index: int = -1
    e_index: int = 4
    assert sub(xs, s_index, e_index) == [10, 20, 30, 40]


def test_sub_ending_greater_than_len_xs() -> None:
    """Testing Sub with Ending Index Value Greater than Length of xs List."""
    xs: list[int] = [10, 20, 30, 40, 50]
    s_index: int = 0
    e_index: int = 17
    assert sub(xs, s_index, e_index) == [10, 20, 30, 40, 50]


def test_sub_extreme() -> None:
    """Testing Sub. with Extreme Values."""
    xs: list[int] = [10**2, 20**2, 30**2, 40**2, 50**2]
    s_index: int = 1
    e_index: int = 5
    assert sub(xs, s_index, e_index) == [20**2, 30**2, 40**2, 50**2]