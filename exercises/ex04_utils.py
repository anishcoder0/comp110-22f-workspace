"""The List Utility Function."""

__author__: str = "730574592"


def all(list_of_int: list[int], one_int: int) -> bool:
    """This function checks if all numbers in list is one_int."""
    count: int = 0
    while count < len(list_of_int):
        if one_int == list_of_int[count]:
            count += 1      
        
        else:
            return False
    
    if len(list_of_int) == 0:
        return False
    else:
        return True
            
    
def max(max_list: list[int]) -> int:
    """This function finds the max number in a list."""
    if len(max_list) == 0:
        raise ValueError("max() arg is an empty List")
    max_num: int = max_list[0]
    max_count: int = 0
    while max_count < len(max_list):
        if max_num > max_list[max_count]:
            max_num = max_num
        else:
            max_num = max_list[max_count]
        max_count += 1
    return max_num


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """This function checks to see if the 2 lists are the same."""
    list_index: int = 0     
    while (list_index < len(list1)) and (list_index < len(list2)):
        if list1[list_index] == list2[list_index]:
            list_index += 1
        else:
            return False
    if list_index == len(list1) and list_index == len(list2):
        return True
    else:
        return False    