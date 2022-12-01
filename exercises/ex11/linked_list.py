"""Utility functions for working with Linked Lists."""

from __future__ import annotations
from typing import Optional

__author__ = "730574592"


class Node:
    """An item in a singly-linked list."""
    data: int
    next: Optional[Node]

    def __init__(self, data: int, next: Optional[Node]):
        """Construct a singly linked list. Use None for 2nd argument if tail."""
        self.data = data
        self.next = next

    def __str__(self) -> str:
        """Produce a string visualization of the linked list."""
        if self.next is None:
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"


def is_equal(lhs: Optional[Node], rhs: Optional[Node]) -> bool:
    """Test if two linked lists are deeply (values and order) equal to one another."""
    if lhs is None and rhs is None:
        return True
    elif lhs is None or rhs is None or lhs.data != rhs.data:
        return False
    else:
        return is_equal(lhs.next, rhs.next)


def last(head: Optional[Node]) -> int:
    """Returns the last value of a Linked List, or raises a ValueError if the list is empty."""
    if head is None:
        raise ValueError("last cannot be called with None")
    else:
        if head.next is not None:
            return last(head.next)
        return head.data


def value_at(head: Optional[Node], index: int) -> int:
    """Return the data of the Node stored at the given index."""
    if head is None:
        raise IndexError("Index is out of bounds on the list.")   
    if index == 0:
        return head.data  
    elif head.data is not None and head.next is not None:
        return value_at(head.next, index - 1)


def max(head: Optional[Node]) -> int:
    """Return the maximum data value in the linked list."""
    if head is None:
        return None
    max_num_list: Optional[int] = max(head.next)
    if max_num_list is None:
        return head.data
    else:
        if head.data > max_num_list:
            return head.data
        else:
            return max_num_list
    

def linkify(items: list[int]) -> Optional[Node]:
    """Return a Linked List of Nodes with the same values, in the same order, as the input list."""
    if len(items) == 0:
        return None
    else:
        items_val: int = items[0]
        next_item: list[int] = linkify(items[1:])
        return Node(items_val, next_item) 


def scale(head: Optional[Node], factor: int) -> Optional[Node]:
    """Return a new linked list of Nodes where each value in the original list is scaled (multiplied) by the scaling factor."""
    if head is None:
        return None
    else:
        scale_num: int = head.data * factor
        new_num: Optional[Node] = scale(head.next, factor)
        return Node(scale_num, new_num)

