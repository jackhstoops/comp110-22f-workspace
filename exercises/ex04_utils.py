"""EX04 - Utils."""

__author__ = "730489241"


def all(int_list: list[int], an_int: int) -> bool:
    """Given list of int + int, return True/False if list int == given int."""
    i = 0
    if len(int_list) == 0:
        return False
    while i < len(int_list):
        if int_list[i] == an_int:
            i += 1
        else:
            return False
    return True


def max(int_list: list[int]) -> int:
    """Given int_list, return largest int."""
    if len(int_list) == 0:
        raise ValueError("max() arg is an empty List")
    max: int = int_list[0]
    i = 0
    while i < len(int_list):
        if max < int_list[i]:
            max = int_list[i]
            i += 1
        else:
            i += 1
    return max


def is_equal(equal_1: list[int], equal_2: list[int]) -> bool:
    """Given 2 lists, compare if they are equal and return True."""
    i = 0
    if len(equal_1) != len(equal_2):
        return False
    while i < len(equal_1) and i < len(equal_2):
        if equal_1[i] == equal_2[i]:
            i += 1
        else:
            return False
    return True