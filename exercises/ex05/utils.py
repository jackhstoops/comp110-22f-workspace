"""EX05 - list Utility Functions."""

__author__ = "730489241"


def only_evens(xs: list[int]) -> list:
    """Checks for only even numbers."""
    i = 0
    evens = []
    while i < len(xs):
        if xs[i] == 0:
            i += 1
        else:
            if xs[i] % 2 == 0:
                evens.append(xs[i])
                i += 1
            else:
                i += 1
    return evens


def concat(one_xs: list[int], two_xs: list[int]) -> list:
    """Adds one_xs and two_xs lists together sequentially."""
    three_xs = []
    i = 0
    while i < len(one_xs):
        three_xs.append(one_xs[i])
        i += 1
    i = 0
    while i < len(two_xs):
        three_xs.append(two_xs[i])
        i += 1
    return three_xs


def sub(xs: list[int], s_index: int, e_index: int) -> list:
    """Creates list within s_index and e_index parameters from xs."""
    i = s_index
    end = e_index
    new_list: list[int] = []
    if i < 0:
        i = 0
    if end <= 0:
        return new_list
    while i < len(xs) and i != end:
        new_list.append(xs[i])
        i += 1
    return new_list