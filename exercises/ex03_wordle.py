"""Actual Wordle Game."""

__author__ = "730574592"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

def contains_char(search_through: str, single_char: str) -> bool:
    """The 2nd paramater will search through the first string to see if it exists in it. If so it returns True, otherwise it returns False"""
    assert len(single_char) == 1
    search_through_index: int = 0

    while search_through_index < len(search_through):
        if single_char == search_through[search_through_index]:
            return True
        else:
            search_through_index += 1
    
    return False

def emojified(guess: str, secret: str) -> str:
    """This function assigns each letter of the guess a emoji box based on its relationship to the secret word."""
    assert len(guess) == len(secret)
    guess_index = 0
    emoji_for_guess: str = ""
    while guess_index < len(secret):
        if guess[guess_index] == secret[guess_index]:
            emoji_for_guess += GREEN_BOX
        elif contains_char(secret, guess[guess_index]) == True:
            emoji_for_guess += YELLOW_BOX
        else:
            emoji_for_guess += WHITE_BOX
        guess_index += 1
    return emoji_for_guess

def input_guess(expected_length: int) -> str:
    """This function prompts the user to enter a guess with expected_length characters. It will keep prompting until it gets its expected answer."""
    guess_word: str = input(f"Enter a {expected_length} character word: ")
    
    while len(guess_word) != expected_length:
        guess_word = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess_word

def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word = "codes"
    turns = 1
    status = False
    while turns < 7 and status == False:
        print(f"=== Turn {turns}/6 ===")
        guess = input_guess(len(secret_word))
        print(emojified(guess,secret_word))
        if guess == secret_word:
            status = True
        else:
            turns += 1
    if status == True:
        print(f"You won in {turns}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")

if __name__ == "__main__":
    main()
