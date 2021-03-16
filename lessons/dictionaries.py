"""Examples of dictionaries"""

# establish a type with a dict[key type, valye type]
# Key type always precedes value type
# Empty dictionary literal is {}
players: dict[str, int] = {}

# Insert a new key-value pair
# Reference keys inside subscription notation, associated values are assigned
players["Brooks"] = 15
players["Love"] = 2
players["Bacot"] = 4 # Intentionally off by one
players["Bacot"] = players["Bacot"] + 1
print(players)
print(players["Brooks"])

# for..in loops will give you each key one-by-one
for player_name in players: 
    print(f"{player_name} -> {players[player_name]}")


# You can have keys and valyes of any types! Notice this is the oppoistie mapping
#that we had above. Additionaly, thi is an example of a dictionary literal
jerseys: dict[int, str] = {15: "Brooks", 2: "Love", 5: "Bacot"}
jerseys[69] = "Best"
print(jerseys)


# The pop method allows you to remove a key_valye pair by its key
# The pop method returns the value associated with the popped key
popped_name: str = jerseys.pop(69)
print(popped_name)
print(jerseys)