"""EX03 - palindromify function."""

__author__: str = "730390102"


def main() -> None:
    """Entrypoint of the program."""
    # Put print statements here to test your function
    print(palindromify("race", False))
    # ex. print(palindromify("race", false))


def palindromify(input: str, type: bool) -> str: 
    """Creates a palindrome."""
    i: int = 1
    new_string: str = input
    if type is True: 
        while i < len(input) + 1  :
            new_string += input[-i]
            i += 1 
        return(new_string)
    else: 
        i = 2
        while i < len(input) + 1  :
            new_string += input[-i]
            i += 1 
        return(new_string)


if __name__ == "__main__":
    main()