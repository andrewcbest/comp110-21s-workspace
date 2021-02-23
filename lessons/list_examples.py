"""some examples of list concepts"""

rolls: list[int] # Declare a variable whose type is list of ints

rolls = [2, 3, 2, 6] # Initialize w/ list literal syntaz

print(f"Length of rolls is {len(rolls)}")
print(f"The last value in the list is {rolls[len(rolls) - 1]}")

from random import randint
rolls.append(randint(1,6)) # Lists's append method adds to the end of the list
print(rolls)

rolls.pop() # :ists's pop method, with no argument, removes the ;ast item of the list
rolls.pop(0) # lists' pop method, one argument, pops a specific index
print(rolls)

words: list[str] = list() # COnstruct an empty list using the list constructor
words.append("Hello")
print(words)
