"""Dictionary related utility functions."""
from csv import DictReader

__author__ = "730574592"

# Define your functions below


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []

    # Open a hnadle to the data file.
    file_handle = open(filename, "r", encoding="utf8")
   
    # Prepare to read the data file as a CSV rather than just strings
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line-by-line.
    for row in csv_reader:
        result.append(row)
    # Close the file when we're done, to free its resources.
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
    """Transform a row oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
        
    return result


def head(column_dict: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Produce a new column-based table with only the first N rows of data for each column."""
    new_dict: dict[str, list[str]] = {}
    for column in column_dict:
        i: int = 0
        values: list[str] = []
        while i < len(column_dict[column]) and i < rows:
            values.append(column_dict[column][i])
            i += 1
        new_dict[column] = values
    return new_dict


def select(column_dict: dict[str, list[str]], copy_list: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with only a specific subset of the original columns."""
    new_dict: dict[str, list[str]] = {}
    for column in copy_list:
        new_dict[column] = column_dict[column]
    return new_dict


def concat(concat_1: dict[str, list[str]], concat_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based table with two column-based tables combined."""
    new_dict: dict[str, list[str]] = {}
    for column in concat_1:
        new_dict[column] = concat_1[column]
    for column in concat_2:
        if column in new_dict:
            for x in concat_2[column]:
                new_dict[column].append(x)
        else:
            new_dict[column] = concat_2[column]
    return new_dict


def count(new_list: list[str]) -> dict[str, int]:
    """Count how many times a value has shown up in the input list."""
    new_dict: dict[str, int] = {}
    for x in new_list:
        if x in new_dict:
            new_dict[x] += 1
        else:
            new_dict[x] = 1
    return new_dict