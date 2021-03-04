"""for...in loop examples."""

# Iterate through each item in a list
letters: list[str] = ["a", "b", "c", "d", "e", "f", "g"]

# Print each letter in the letters list
print("each letter...")
for s in letters:
    print(s)


# Print every othe letter in letters list
print("every other letter...")
for i in range(1, len(letters), 2):
    print(letters[i])


# Iterate through each index in a sequence
for i in range(len(letters)):
    print(f"i: {i} - letters[i]: {letters[i]}")