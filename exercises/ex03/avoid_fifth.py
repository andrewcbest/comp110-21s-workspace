"""EX03 - avoid_fifth function."""

__author__: str = "730390102"


def main() -> None:
    """Entrypoint of the program."""
    print(avoid_fifth("Hello"))
    print(avoid_fifth("The sentence we have here possesses E's galore!"))
    # Put print statements here to test your function
    # ex. print(avoid_fifth("hello there"))


def avoid_fifth(input: str) -> str: 
    """Removes e's and E's."""
    i: int = 0
    new_str: str = ""
    while i < len(input):
        if input[i] != "e" and input[i] != "E":
            new_str += input[i]
        i += 1
    return(new_str)


if __name__ == "__main__":
    main()