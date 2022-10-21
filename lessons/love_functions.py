"""Some tender, loving functions."""

def love(subject: str) -> str:
    """Given a subject as a parameter, returns a loving string."""
    return f"I love you {subject}!"

print(love("mom"))

def spread_love(to: str, n: int) -> str:
    """Generates a str repeating a loving message n times."""
    love_note = ""
    counter = 0
    while counter < n:
        counter += 1
        love_note += love(to) + "\n"
    return love_note

