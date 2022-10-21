"""Dictionary test for exercise EX07."""


__author__: str = "730574592"


from exercises.ex07.dictionary import count, invert, favorite_color


def test_invert_normal() -> None:
    """Should give normal output."""
    example: dict[str, str] = {"a": "b", "c": "d"}
    assert invert(example) == {"b": "a", "d": "c"}


def test_invert_with_one_case() -> None:
    """Invert with only 1 dictionary pair."""
    example: dict[str, str] = {"a": "b"}
    assert invert(example) == {"b": "a"}


def test_invert_with_empty_dict() -> None:
    """Invert with no pairs."""
    example: dict[str, str] = {}
    assert invert(example) == {}


def test_favorite_color_normal() -> None:
    """Should return normal output."""
    example: dict[str, str] = {"K": "Orange", "J": "blue"}
    assert favorite_color(example) == "Orange"


def test_favorite_color_with_one_case() -> None:
    """Favorite color with only 1 test case."""
    example: dict[str, str] = {"K": "orange"}
    assert favorite_color(example) == "orange"


def test_favorite_color_no_cases() -> None:
    """Favorite Color without any input."""
    example: dict[str, str] = {}
    assert favorite_color(example) == ""


def test_count_normal() -> None:
    """Count function that is normal."""
    example: list[str] = ["Anime", "Jake", "Ian", "Anish", "Anish"]
    assert count(example) == {"Anime": 1, "Jake": 1, "Ian": 1, "Anish": 2}


def test_count_with_one_case() -> None:
    """Count function with only 1 test case."""
    example: list[str] = ["Anime"]
    assert count(example) == {"Anime": 1}


def test_count_with_no_case() -> None:
    """Count function without any test cases."""
    example: list[str] = []
    assert count(example) == {}