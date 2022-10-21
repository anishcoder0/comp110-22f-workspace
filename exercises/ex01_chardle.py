"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730574592"

word: str = input("Enter a 5-character word: ")
if len(word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
single: str = input("Enter a single character: ")
if single == " " or len(single) != 1:
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + single + " in " + word)
repeat = 0

if single == word[0]:
    print(single + " found at index 0")
    repeat += 1

if single == word[1]:
    print(single + " found at index 1")
    repeat += 1

if single == word[2]:
    print(single + " found at index 2")
    repeat += 1

if single == word[3]:
    print(single + " found at index 3")
    repeat += 1

if single == word[4]:
    print(single + " found at index 4")
    repeat += 1
if repeat == 0:
    print("No instances of " + single + " found in " + word)
if repeat > 1:
    print(repeat, "instances of " + single + " found in " + word)
if repeat == 1:
    print(repeat, "instance of " + single + " found in " + word)
