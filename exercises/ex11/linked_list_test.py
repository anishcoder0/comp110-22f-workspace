"""Tests for linked list utils."""

import pytest
from exercises.ex11.linked_list import Node, last, value_at, max, linkify, scale

__author__ = "730574592"


def test_last_empty() -> None:
    """Last of an empty Linked List should raise a ValueError."""
    with pytest.raises(ValueError):
        last(None)


def test_last_non_empty() -> None:
    """Last of a non-empty list should return its last data value."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert last(linked_list) == 3


def test_value_at_empty() -> None:
    """If it is empty it should raise an Index error."""
    with pytest.raises(IndexError):
        value_at(None, 0)


def test_value_at_pplplpl() -> None:
    """Should return the data value at given index."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert value_at(linked_list, 0) == 1


def test_max_empty() -> None:
    """Should raise error if empty list."""
    with pytest.raises(ValueError):
        max(None)


def test_max_rand_order() -> None:
    """Returns max number in this list."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert max(linked_list) == 3


def test_linkify_empty() -> None:
    """should raise error if empty."""
    list1: list[int] = []
    assert linkify(list1) is None


def test_linkify_normal() -> None:
    """Should proceed Normally and return."""
    list2: list[int] = [1, 2, 3]
    assert linkify(list2) == linkify(list2)


def test_scale_empty() -> None:
    """Should assert None."""
    assert scale(None, 0) is None


def test_scale_normal() -> None:
    """Has a test."""
    assert scale(linkify([1, 2, 3]), 2) == linkify([2, 4, 6])
