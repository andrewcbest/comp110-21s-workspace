"""EX03 - avoid_fifth function."""

__author__: str = "730390102"


def main() -> None:
    """Entrypoint of the program."""
    print(avoid_fifth("Hello"))
    print(avoid_fifth("The sentence we have here possesses E's galore!"))
    # Put print statements here to test your function
    # ex. print(avoid_fifth("hello there"))


def avoid_fifth(text_input: str) -> str:
    """Will remove any E's!"""
    i = 0
    text_list: list[str] = []
    while i < len(text_input):
        ordinal: int = ord(text_input[i])
        if ordinal != 69 and ordinal != 101:
            text_list.append(chr(ordinal))
        i += 1
    new_text: str
    new_text = ""
    for i in text_list:
        new_text += i 
    return(new_text)


if __name__ == "__main__":
    main()