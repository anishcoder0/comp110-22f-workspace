"""Example of the tyiple and range sequences."""
# An example of a tuple withoiut type aliasing
goat: tuple[str, int] = ("MJ", 23)
# Tuples are sequences, so they're 0-indexed
print(goat[0])
print(goat[1])

# sequences have lengths
print(len(goat))

# sequences are iterable with for... in loops
# Meaning you can loop over them with for...in
for item in goat:
    print(item)
# Printing a tuple produces its literal syntax
print(goat)
# print both items on the same line

print(f"{goat[0]} is number {goat[1]}")

# Tuples, unlike lists, are imutable
# Which means we cannot reassign items, nor append, nor pop, etc.
# goat[0] = "LBJ"

# we can "invent" our own type with a type alias
Player = tuple[str, int]

# Once we've aliased a type, we can create variables of that type

unc_poy: Player = ("Bacot", 5)

# In a strange world, where jersey number changes...
unc_poy = (unc_poy[0], unc_poy[1] + 1)

# A range is another common sequence type
zero_to_nine: range = range(0, 10, 1)

# We can access items of the range
print(zero_to_nine[0])
print(zero_to_nine[9])

for i in zero_to_nine:
    print(i)

# We can have different steps for more control
odds_to_99: range = range(1, 100, 2)
for i in odds_to_99:
    print(i)

names: list[str] = ["Kris", "Alyssa", "Micheal", "Lebron"]
for i in range(len(names)):
    print(f"{i}. {names[i]}")

