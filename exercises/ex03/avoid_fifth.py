"""EX03 - avoid_fifth function."""

__author__: str = "730390102"


def main() -> None:
    """Entrypoint of the program."""
    print(avoid_fifth("Hello"))
    print(avoid_fifth("The sentence we have here possesses E's galore!"))
    # Put print statements here to test your function
    # ex. print(avoid_fifth("hello there"))


def avoid_fifth(str):
    i: int = 0
    new_str: str = ""
    while i < len(str):
        if str[i] != "e" and str[i] != "E":
            new_str += str[i]
        i += 1
    return(new_str)


if __name__ == "__main__":
    main()