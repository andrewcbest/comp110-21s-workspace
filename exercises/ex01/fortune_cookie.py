"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730390102"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
print("Your fortune cookie says...")

cookie: int = randint(1 , 4)

if cookie == 1:
    print("duke will lose today!")
else:
    if cookie == 2:
        print("the force is strong with you.")
    else:
        if cookie == 3:
            print("tommorow will be the best day of your life!")
        else:
            print("I better not read you this one.")

print("Now, go spread positive vibes!")


