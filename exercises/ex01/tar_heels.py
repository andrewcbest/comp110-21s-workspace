"""An exercise in remainders and boolean logic."""

__author__ = "730390102"


# Begin your solution here...
number: str = input("Enter an int:")

num = int(number)

if num % 14 == 0: 
    print("TAR HEELS")
else:
    if num % 7 == 0: 
        print("HEELS")
    else:
        if num % 2 == 0:
            print("TAR")
        else:
            print("CAROLINA")