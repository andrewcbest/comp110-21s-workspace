""""Choose your own adventure project."""

from random import randint

__author__ = "730390102"

points: int = 0

def main() -> None:
    """The entrypoint of the program."""
    greet()
    choice: str = input("easy, medium, hard, or end? ")
    if choice == "easy":
        easy()
    else: 
        if choice == "hard":
            hard()
        else:
            end()


def greet() -> None:
    """Greets the player."""
    global name
    name = str(input("What is your name? "))
    print(f"Hello {name}! This is a number guessing game. Good lucK!")


def easy() -> None:
    """Number guessing game where the user guesses between 1 and 2"""
    print("In this game, you will guess if a number is 1 or 2! 50/50 shot! Good luck. ")
    i: int = 1
    while(i < 11):
        num: str = str(randint(1,2))
        guess: str = (input(f"Round {i}! Please enter guess: "))
        if guess == num: 
            global points
            points += 2
            print("Correct!")
        else: 
            points += 1
            print("Nope.")
        print(f"Round: {i} / 10. Score: {points}")
        i += 1
    end()

def end() -> None:
    """Ends the game."""
    print(f"Thanks for playing, {name}! Score: {points}")


if __name__ == "__main__":
    main()
