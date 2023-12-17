print("Variable name should start with alpha-numeric characters, _ or string");
print("Variable name should not start with numbers, hyphen");
print("Variable names are case sensitive");

greet = 'welcome' # String
castToString = str(3)
# Find Variable Type
print(f">>> Type of greet is {type(greet)}")
print(f">>> Type of castToString is {type(castToString)}")

# Number Data Type Variables
currentYear = 2024 # int for year
print(f"\n>>> Type of currentYear is {type(currentYear)}")
castToInteger = int(2024)

weight = 75.50 # Float for Weight in Kg
print(f"\n>>> Type of weight is {type(weight)}")
castToFloat = float('75.50')
print(f">>> Type of castToFloat is {type(castToFloat)}")

fruits = ["apple", "banana", "cherry"] # List for fruits
print(f"\n>>> Type of fruits is {type(fruits)}")
# castToFloat = float('75.50')
# print(f">>> Type of castToFloat is {type(castToFloat)}")