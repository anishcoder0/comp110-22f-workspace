"""One Shot Wordle Exercise"""



__author__: str = "730574592"
#all my basic variables that need to be initialized
secret_word: str = "python"
guess: str = input(f"What is your {len(secret_word)}-letter guess? " )
count = 0
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
index_of_word: int = 0
emoji_for_guess: str = ""

#While loop to check whether guess is equal to secret word
while len(guess) != len(secret_word):
    guess = input(f"That was not {len(secret_word)} letters! Try again: ") 

#checks to see what emoji each letter in guess is
while index_of_word < len(secret_word):
    does_character_exist = False
    secret_word_indices = 0
    
    if guess[index_of_word] == secret_word[index_of_word]:
        emoji_for_guess += GREEN_BOX
    else:
        while does_character_exist != True and secret_word_indices < len(secret_word):
            if guess[index_of_word] == secret_word[secret_word_indices]:
                does_character_exist = True
                emoji_for_guess += YELLOW_BOX
            else:
                secret_word_indices += 1
        if does_character_exist == False:
            emoji_for_guess += WHITE_BOX
    
    index_of_word += 1

#printing out the results and the boxes
if guess != secret_word:
    print(emoji_for_guess)
    print("Not quite. Play again soon!")
else:
    print(emoji_for_guess)
    print("Woo! You got it!")





        

