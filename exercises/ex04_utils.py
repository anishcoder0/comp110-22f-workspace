"""The List Utility Function."""

__author__: str = "730574592"


def all(list_of_int: list[int], one_int: int) -> bool:
    count = 0
    while count < len(list_of_int):
        if one_int == list_of_int[count]:
            count += 1
        else:
            return False
    
    return True
            
    
def max(max_list: list[int]) -> int:
    if len(max_list) == 0:
        raise ValueError("max() arg is an empty List")
    max_num = max_list[0]
    maxcount = 1
    while maxcount < len(max_list):
        if max_num > max_list[maxcount]:
            max_num = max_num
        else:
            max_num = max_list[maxcount]
    return max_num

def is_equal(list1: list[int], list2: list[int]) -> bool:
    list_index = 0     
    while (list_index < len(list1)) and (list_index < len(list2)):
        if list1[list_index] == list2[list_index]:
            list_index += 1
        else:
            return False
    return True
