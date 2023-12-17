print('\n >>>> Variable Example');
print("Variable name should start with alpha-numeric characters, _ or string");
print("Variable name should not start with numbers, hyphen");
print("Variable names are case sensitive");

# Multiple Variables
print("\n>>>> Multiple Variables");
x, y, z = 1, 2, "Three"
print(f"X: {x}, Y: {y}, Z: {z}")

# One Value to Multiple Variables
print("\n>>>> One Value to Multiple Variables");
previous = current = next = 1
print(f"previous: {previous}, current: {current}, next: {next}");

# Unpack a Collection
print("\n>>>> Unpack a Collection: list, tuple");
fruits = ["apple", "banana", "cherry"]
firstFruit, secondFruit, thirdFruit = fruits
print(f"firstFruit: {firstFruit}, secondFruit: {secondFruit}, thirdFruit: {thirdFruit}")
