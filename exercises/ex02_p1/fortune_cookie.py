"""Fortune cookie exercise redux as a structured program."""

from random import randint

__author__ = "730390102"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print("Your fortune cookie says...")
    # TODO 2: Print the result of calling your fortune_cookie function.
    print(fortune_cookie())
    print("Now, go spread positive vibes!")


# TODO 1: Define your fortune_cookie function here.

def fortune_cookie() -> str:
    """Will give the user one of four fortunes."""
    cookie: int = randint(1, 4)
    if cookie == 1:
        return("duke will lose today!")
    else:
        if cookie == 2:
            return("the force is strong with you.")
        else:
            if cookie == 3:
                return("tommorow will be the best day of your life!")
            else:
                return("I better not read you this one.")

# Python Idiom for "starting" the program when run as a module.
# The special dunder variable __name__ will be "__main__" when run as module. 
if __name__ == "__main__":
    main()
    
 
    