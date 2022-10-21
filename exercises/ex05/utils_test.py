"""Test for utils function."""


__author__: str = "730574592"


from exercises.ex05.utils import concat, sub
from utils import only_evens


def test_only_evens_empty() -> None:
    """Only_evens case with empty list."""
    xs: list[int] = []
    assert only_evens(xs) == []
 

def test_only_evens_no_evens() -> None:
    """Only_evens case with 1 even."""
    test_list: list[int] = [1, 2, 3, 5]
    assert only_evens(test_list) == [2]


def test_only_evens_all_evens() -> None:
    """Only_evens case with all evens."""
    test_list: list[int] = [2, 4, 6, 8, 10]
    assert only_evens(test_list) == [2, 4, 6, 8, 10]


def test_only_evens_all_odds() -> None:
    """Only_evens case with all odds."""    
    test_list: list[int] = [1, 3, 5]
    assert only_evens(test_list) == []


def test_concat_no_items() -> None:
    """No items in both lists."""   
    test_list1: list[int] = []
    test_list2: list[int] = []
    assert concat(test_list1, test_list2) == []


def test_concat_same_items() -> None:
    """Same numbers but in opposite order from list."""    
    test_list1: list[int] = [1, 2, 3]
    test_list2: list[int] = [3, 2, 1]
    assert concat(test_list1, test_list2) == [1, 2, 3, 3, 2, 1]


def test_concat_with_1_empty_list() -> None:
    """One of the test lists is empty."""    
    test_list1: list[int] = [1, 2, 3]
    test_list2: list[int] = []
    assert concat(test_list1, test_list2) == [1, 2, 3]


def test_sub_with_smaller_last_index() -> None:
    """Returns empty list if last index is smaller than start."""
    test_list: list[int] = [1, 2, 3, 4, 5]
    assert sub(test_list, 2, 1) == []


def test_sub_with_normal_case() -> None:
    """Should return a normal range."""    
    test_list: list[int] = [1, 2, 3, 4, 5]
    assert sub(test_list, 1, 3) == [2, 3]


def test_sub_with_negative_start_index() -> None:
    """Start index should be at 0."""    
    test_list: list[int] = [1, 2, 3, 4, 5]
    assert sub(test_list, -1, 3) == [1, 2, 3]