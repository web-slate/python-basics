print('\n >>>> Data Type Example')
print('15 Types of Data Types')
print('>>>> 1st. Text Type')
print('1. string\n')
print('>>>> 2nd Numeric Type')
print('2. int, 3. float, 4. complex\n')
print('>>>> 3rd Sequence Type')
print('5. list, 6. tuple, 7. range\n')
print('>>>> 4th Mapping Type')
print('8. dict\n')
print('>>>> 5th Set Type')
print('9. set, 10. frozenset\n')
print('>>>> 6th Boolean Type')
print('11. bool\n')
print('>>>> 7th Binary Type')
print('11. bytes, 12. byteArray, 13. memoryView\n')
print('>>>> 8th None Type')
print('11. None\n')

greet = 'welcome' # String
castToString = str(3)
# Find Variable Type
print(f">>> Type of greet is {type(greet)}")
print(f">>> Type of castToString is {type(castToString)}")

# Number Data Type Variables
currentYear = 2024 # int for year
print(f"\n>>> Type of currentYear is {type(currentYear)}")
castToInteger = int(2024.00)
print(f">>> Type of castToInteger is {type(castToInteger)}")

weight = 75.50 # Float for Weight in Kg
print(f"\n>>> Type of weight is {type(weight)}")
castToFloat = float('75.50')
print(f">>> Type of castToFloat is {type(castToFloat)}")

print("\n>>> List Type")
fruits = ["apple", "banana", "cherry"] # List for fruits
print(f">>> Type of fruits is {type(fruits)}")
fruits.append("grapes")
print('Fruits List: ', fruits)

print("\n>>> Tuple Type")
configuration = ('2MB','30 Minutes') # Tuple 
print(f">>> Type of configuration is {type(configuration)}")
print('configuration Tuple: ', configuration)

print("\n>>> Dict Type")
employeeDictionary = {"name" : "John", "age" : 36} # Dict
print(f">>> Type of employeeDictionary is {type(employeeDictionary)}")
print('employee dictionary: ', employeeDictionary)
config = {True : "dummyValue", 1 : "actualConfigValue"} # Dict key will same True but value will be overriden.
print('config dictionary: ', config)

print("\n>>> Boolean Type")
eligibleToVote = True # Boolean
print(f">>> Type of eligibleToVote is {type(eligibleToVote)}")
print('eligibleToVote: ', eligibleToVote)

# TODO
# Add Bytes
# Add None examples