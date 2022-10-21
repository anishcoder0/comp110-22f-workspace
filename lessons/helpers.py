"""Demonstrate defining a module imported elsewhere."""

THE_ANSWER: int = 42
def powerful(x: float, n: float) -> float:
    """Raise x to the power of n."""
    return x**n

def main() -> None:
    print(powerful(2,10))
    print("helpers.py run as a module")