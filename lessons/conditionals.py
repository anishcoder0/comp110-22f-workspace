"""An example of conditional (if-else) statements"""
SECRET: int = 3
print("I'm thinking of a number between 1-5, what is it?")
guess: int = int(input("What is your guess:\n"))

if guess == SECRET:
    print("You Guessed Correctly!!!!!")
    print("Have a Wonderfull Day")
else:
    print("Sorry, you guesed incorrectly :(")
    print("Try running the program again!")
print("Game Over")