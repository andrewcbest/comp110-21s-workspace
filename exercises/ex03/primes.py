"""EX03 - prime functions."""

__author__: str = "730390102"


def main() -> None:
    """Entrypoint of the program."""
    # Put print statements here to test your function
    print(is_prime(5))
    print(is_prime(10))
    print(is_prime(169))
    print(list_primes(1, 5000))
    # ex. print(is_prime(5)), print(list_primes(10, 20))


def is_prime(num: int) -> bool :
    """Determines if an integer is prime."""
    i: int = 2
    if num == 1:
        return(False)
    while i < num : 
        if num % i == 0 :
            return(False)
        i += 1  
    return(True)


def list_primes(num1: int, num2: int) -> list :
    """Finds the primes within bewteen two integers."""
    primes: list = []
    i: int = num1
    while i < num2 :   
        if is_prime(i) is True:
            primes.append(i)
        i += 1
    return primes



if __name__ == "__main__":
    main()