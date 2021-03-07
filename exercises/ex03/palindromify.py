"""EX03 - palindromify function."""

__author__: str = "730390102"


def main() -> None:
    """Entrypoint of the program."""
    # Put print statements here to test your function
    print(palindromify("race", False))
    # ex. print(palindromify("race", false))


def palindromify(str, bool):
    """Creates a palindrome."""
    if bool == True: 
        i: int = 1
        new_string: str = str
        while i < len(str) + 1 :
            new_string += str[-i]
            i += 1 
        return(new_string)
    else: 
        i: int = 2
        new_string: str = str
        while i < len(str) + 1 :
            new_string += str[-i]
            i += 1 
        return(new_string)


if __name__ == "__main__":
    main()