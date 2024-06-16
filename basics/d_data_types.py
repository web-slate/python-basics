from stylepy import h1, h2, h3, h4, h5, h6
from stylepy import blockquote
from stylepy import pretty_json
h1('\n >>>> Data Type Example')
h2('15 Types of Data Types')
h3('>>>> 1st. Text Type')
h4('1. string\n')
print('>>>> 2nd Numeric Type')
h4('2. int, 3. float, 4. complex\n')
print('>>>> 3rd Sequence Type')
h4('5. list, 6. tuple, 7. range\n')
print('>>>> 4th Mapping Type')
h4('8. dict\n')
print('>>>> 5th Set Type')
h4('9. set, 10. frozenset\n')
print('>>>> 6th Boolean Type')
h4('11. bool\n')
print('>>>> 7th Binary Type')
h4('11. bytes, 12. byteArray, 13. memoryView\n')
print('>>>> 8th None Type')
h4('11. None\n')

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

h3("\n>>> List Type")
fruits = ["apple", "banana", "cherry"] # List for fruits
print(f">>> Type of fruits is {type(fruits)}")
fruits.append("grapes")
h4('Fruits List: ', fruits)
blockquote(fruits) # blockquote

h3("\n>>> Tuple Type")
configuration = ('2MB','30 Minutes') # Tuple 
print(f">>> Type of configuration is {type(configuration)}")
print('configuration Tuple: ', configuration)

h3("\n>>> Dict Type")
employeeDictionary = {"name" : "John", "age" : 36} # Dict
print(f">>> Type of employeeDictionary is {type(employeeDictionary)}")
pretty_json(employeeDictionary) #pretty json
print('employee dictionary: ', employeeDictionary)
config = {True : "dummyValue", 1 : "actualConfigValue"} # Dict key value will be same True or 1 so latest value will be overriden.
print('config dictionary: ', config)

h3("\n>>> Boolean Type")
eligibleToVote = True # Boolean
print(f">>> Type of eligibleToVote is {type(eligibleToVote)}")
print('eligibleToVote: ', eligibleToVote)

sunRiseToday = 'east'
sunRiseTodayInWest = True if sunRiseToday == 'west' else False
print(f"\n>>> Type of sunRiseTodayInWest is {sunRiseTodayInWest}")
print('sunRiseTodayInWest: ', sunRiseTodayInWest)

# TODO
# Add Bytes
# Add None examples