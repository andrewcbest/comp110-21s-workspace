""""Choose your own adventure project. For the above and beyond, there is a game loop."""
"""After each game, the user gets the opportunity to play one of the games again or quit."""
"""Also, there are four options, more than the three required: easy, medium, hard, and end."""


from random import randint

__author__ = "730390102"

SMILEY_DEVIL = "\U0001F608"

points: int = 0

def main() -> None:
    """The entrypoint of the program."""
    global points
    greet()
    play_again: str = "yes"
    while play_again == "yes":
        choice: str = input("easy, medium, hard, or end? ")
        if choice == "easy":
            easy()
            play_again = input(f"Score: {points}. Would you like to play again? (yes/no)")
        else: 
            if choice == "medium":
                points = medium(points)
                play_again = input(f"Score: {points}. Would you like to play again? (yes/no)")
            else:
                if choice == "hard":
                    points = hard(points)
                    play_again = input(f"Score: {points}. Would you like to play again? (yes/no)")
                else:
                    play_again = "no"
    end()


def greet() -> None:
    """Greets the player."""
    global name
    name = str(input("What is your name? "))
    print(f"Hello, {name}! This is a number guessing game. Good lucK!{SMILEY_DEVIL}")


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


def medium(points: int) -> int:
    """Number guessing game where the user guesses number 1 to 5."""
    print("In this game, the number to be guessed is between 1 and 5. Good luck!")
    i: int = 1
    while(i < 11):
        num: str = str(randint(1,5))
        guess: str = (input(f"Round {i}! Please enter guess: "))
        if guess == num: 
            points += 5
            print("Correct!")
        else: 
            points += 1
            print(f"Nope, the number was {num}")
        print(f"Round: {i} / 10. Score: {points}")
        i += 1
    return points


def hard(points: int) -> int:
    """Number guessing game where the user guesses number 1 to 10."""
    print("In this game, the number to be guessed is between 1 and 10. Good luck!")
    i: int = 1
    while(i < 11):
        num: str = str(randint(1,10))
        guess: str = (input(f"Round {i}! Please enter guess: "))
        if guess == num: 
            points
            points += 10
            print("Correct!")
        else: 
            points += 1
            print(f"Nope, the number was {num}")
        print(f"Round: {i} / 10. Score: {points}")
        i += 1
    return points


def end() -> None:
    """Ends the game."""
    print(f"Thanks for playing, {name}! Score: {points}")


if __name__ == "__main__":
    main()
