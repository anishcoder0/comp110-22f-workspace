"""Where I will implement my function skeleton for Exercise 05."""

__author__: str = "730574592"


def only_evens(int_list: list[int]) -> list[int]:
    """Function that takes only even numbers into list."""
    index: int = 0
    even_list: list[int] = []
    while index < len(int_list):
        if (int_list[index]) % 2 == 0:
            even_list.append(int_list[index])
        index += 1
    return even_list


def concat(list1: list[int], list2: list[int]) -> list[int]:
    """Function that concatanates both lists."""
    new_list: list[int] = []
    index: int = 0
    while index < len(list1):
        new_list.append(list1[index])
        index += 1
    index: int = 0
    while index < len(list2):
        new_list.append(list2[index])
        index += 1
    return new_list


def sub(int_list: list[int], first_index: int, last_index: int) -> list[int]:
    """Function that takes a certain range from the list and appends into another."""
    empty_list: list[int] = []
    if first_index < 0:
        first_index = 0
    if last_index > len(int_list):
        last_index = len(int_list)
    if (len(int_list) == 0) or (first_index > len(int_list)) or (last_index <= 0):
        return empty_list
    while first_index < last_index:
        empty_list.append(int_list[first_index])
        first_index += 1

    return empty_list