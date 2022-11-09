"""EX 08 - Utility Functions."""

__author__ = "730489241"


from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of csv into a table."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    
    first_row: dict[str, str] = row_table[0]
    for column in first_row: 
        result[column] = column_values(row_table, column)
    return result


def head(given: dict[str, list[str]], N: int) -> dict[str, list[str]]:
    """Produce a new column-based table, given only the first N rows of data for each column."""
    result: dict[str, list[str]] = {}
    for column in given:
        if N >= len(given[column]):
            return given
        else: 
            first_n_values: list[str] = []
            i: int = 0
            while i < N:
                value: str = given[column][i]
                first_n_values.append(value)
                i += 1
            result[column] = first_n_values
    return result

def count(a_list: list[str]) -> dict[str, int]:
    return count

def select(given: dict[str, list[str]], column_names: list[str]) -> dict[str, list[str]]:
    """Produce new column-based table given only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}
    for column in column_names:
        result[column] = given[column]
    return result


def concat(first: dict[str, list[str]], second: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based table with 2 column-based combined."""
    result: dict[str, list[str]] = {}
    for strings in first: 
        result[strings] = first[strings]
    for strings in second:
        if strings in result: 
            for items in second[strings]:
                result[strings].append(items)
        else:
            result[strings] = second[strings]
    return result