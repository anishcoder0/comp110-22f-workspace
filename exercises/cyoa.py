"""My game about stopping a hurricane."""
__author__ = "730574592"
import random
points: int = 0
player: str = ""
NAMED_CONSTANT = "\U00000000"
MISSION_HAPPY_EMOJI: str = "\U0001F600" 
MISSION_SAD_EMOJI: str = "\U0001F61E"
INSTA_STOP_CONGRATS_EMOJI: str = "\U0001F389"
INSTA_STOP_DEAD_EMOJI: str = "\U0001faa6"
hurricane: int = 0
living = True


def main() -> None:
    greet()
    while living is True:
        if points > 900:
            end_game()
        elif points < 0:
            end_game()
        options: str = int(input("Welcome to the game. Enter 1 for Missions, Enter 2 to try and stop the Hurricane, or enter 3 to quit. \n"))
        options
        if options == 1:
            Missions()
        elif options == 2:
            Insta_Stop(points)
        elif options == 3:
            end_game()
        else:
            print("Please enter the avaliable options!")
    if living is not True:
        end_game()


def greet() -> None:
    global player
    player = input('Hello! Welcome to "Stop the Hurricane". What is your name?\n')
    player


def Missions() -> None:
    global player
    global points
    global living
    status: bool = False
    """Procedure that will allow Player to stop the Hurricane"""
    print(f"Welcome {player}. This will be your chance to stop the hurricane in its path before it destroys you.")
    print(f"Welcome to the Multiplication Challenge {player}! Answer the question correctly to increase your safety range! ")
    while status is False:
        random_number_1: int = random.randint(0, 10)
        random_number_2: int = random.randint(0, 10)
        if points <= 0:
            print("You have lost! The hurricane reached you and left you paralyzed. Try again next time!")
            living = False
            quit()
        question_1: int = int(input(f"What is {random_number_1} * {random_number_2}:\n"))
        question_1
        if question_1 is (random_number_1 * random_number_2):
            print(f"Your correct! You have now increased your safety range!{MISSION_HAPPY_EMOJI}")
            points += 1
            print(f"You now have {points} points!")
            status = True
        elif question_1 != (random_number_1 * random_number_2):
            print(f"Your incorrect! You have traveled closer to hurricane!{MISSION_SAD_EMOJI}")
            points -= 1
            print(f"you only have {points} points left. If you reach 0 points, the hurricane will reach you!")
            status = True


def Insta_Stop(points: int) -> int:
    global player
    global hurricane
    global living
    status: bool = False
    print(f"Hello {player}, this is your chance to stop the hurricane instantly! But beware, if you decide to this but lose, you will lose the game instantly!")
    decision: str = int(input("Would you like to embark on this mission? Type 1 if yes or 2 for no.\n"))
    while status is False:
        Hard_random_number_1: int = random.randint(0, 100)
        Hard_random_number_2: int = random.randint(0, 100)
        if decision == 1:
            print("Answer the question to instantly stop the hurricane!")
            question: str = int(input(f"{player}, what is {Hard_random_number_1} * {Hard_random_number_2}: \n"))
        if question == (Hard_random_number_1 * Hard_random_number_2):
            print(f"Your Correct! You have gone far enough and the hurricane will not reach you! Congrats. {INSTA_STOP_CONGRATS_EMOJI}")
            points += 1000
            status = True
        elif question != (Hard_random_number_1 * Hard_random_number_2):
            print(f"Your incorrect! You were teleported in the hurricane and have died! {INSTA_STOP_DEAD_EMOJI}")
            living = False
            status = True
    return print(f"You now have {points} points. ")


def end_game() -> None:
    global points
    global hurricane
    print(f"Thanks for playing {player}!")
    if living is not True:
        print(f"Unfortuntely the hurricane reached you and killed you. You had a grand total of {points} points. ")
        quit()
    elif living is True:
        print(f"Congrats! You survived the hurricane and won finished with a grand total of {points} points. ")
        quit()


if __name__ == "__main__":
    main()