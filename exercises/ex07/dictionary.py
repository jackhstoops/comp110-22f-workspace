"""EX07 - Dictionary Functions."""

__author__ = "730489241"


def invert(xs: dict[str, str]) -> dict[str, str]:
    """Color a dict[str, str], returns a dict[str, str] that inverts kexs & values."""
    ans: str
    compare: str
    for key in xs:
        ans = key
        for key in xs:
            compare = key
            if ans != compare and xs[ans] == xs[compare]:
                raise KeyError("Please enter a different key")
    result: dict[str, str] = {}
    for key in xs:
        result[xs[key]] = key
    return result


def favorite_color(xs: dict[str, str]) -> str:
    """Return the favorite color."""
    print(f"color dictionary is {xs}") 
    color: list[str] = list()
    for key in xs: 
        color.append(xs[key])
    print(f"The list of colors is {color}")
    print(color)
    result: dict[str, int] = {}

    for item in color:
        if item in result: 
            result[item] += 1
        else: 
            result[item] = 1
    print(result)
    max_value: str = ""
    for key in result:
        compare = key
        for key in result:
            two_compare = key
            if result[compare] > result[two_compare]:
                print(compare)
                print(two_compare)
                print(result[compare] >= result[two_compare])
                max_value = compare
            else:
                if len(result) == 1:
                    max_value = compare
                else:
                    if result[compare] == result[two_compare] and compare != two_compare:
                        max_value = two_compare
    print(f"max: {max_value}")
    return max_value


def count(xs: list[str]) -> dict[str, int]:
    """Given a list of string, the function will return a dictionary."""
    print(xs)
    result: dict[str, int] = {}
    for item in xs:
        if item in result: 
            result[item] += 1
        else: 
            result[item] = 1
    print(result)
    return result