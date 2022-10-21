"""Actual Wordle Game."""

__author__ = "730574592"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(search_through: str, single_char: str) -> bool:
    """The 2nd paramater will search through the first string to see if it exists in it. If so it returns True, otherwise it returns False."""
    assert len(single_char) == 1
    search_through_index: int = 0
    # the while loops uses the single character and returns true if found in the word.
    while search_through_index < len(search_through):
        if single_char == search_through[search_through_index]:
            return True
        else:
            search_through_index += 1
    
    return False


def emojified(guess: str, secret: str) -> str:
    """This function assigns each letter of the guess a emoji box based on its relationship to the secret word."""
    assert len(guess) == len(secret)
    guess_index: int = 0
    emoji_for_guess: str = ""
    # if the guess index is equal to the secret index, then a green box is returned.
    while guess_index < len(secret):
        if guess[guess_index] is secret[guess_index]:
            emoji_for_guess += GREEN_BOX
    # returns yellow if word is in the secret but not in correct position.
        elif contains_char(secret, guess[guess_index]) is True:
            emoji_for_guess += YELLOW_BOX
    # returns white if letter is not in word
        else:
            emoji_for_guess += WHITE_BOX
        guess_index += 1

    return emoji_for_guess


def input_guess(expected_length: int) -> str:
    """This function prompts the user to enter a guess with expected_length characters. It will keep prompting until it gets its expected answer."""
    guess_word: str = input(f"Enter a {expected_length} character word: ")
    # while loop to make sure the user enters the correct number of characters
    while len(guess_word) != expected_length:
        guess_word = input(f"That wasn't {expected_length} chars! Try again: ")

    return guess_word


# final function that combines everything to make the wordle!
def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"
    turns: int = 1
    status: bool = False
    # actual loop that combines all the functions to make the wordle.
    while turns < 7 and not status:
        print(f"=== Turn {turns}/6 ===")
        guess = input_guess(len(secret_word))
        print(emojified(guess, secret_word))
        if guess == secret_word:
            status = True
        else:
            turns += 1
    if status is True:
        print(f"You won in {turns}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()
