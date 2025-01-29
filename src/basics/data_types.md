# Data Types Example

## 15 Types of Data Types

### 1. Text Type
- String (`str`)

### 2. Numeric Type
- Integer (`int`), Float (`float`), Complex (`complex`)

### 3. Sequence Type
- List (`list`), Tuple (`tuple`), Range (`range`)

### 4. Mapping Type
- Dictionary (`dict`)

### 5. Set Type
- Set (`set`), Frozen Set (`frozenset`)

### 6. Boolean Type
- Boolean (`bool`)

### 7. Binary Type
- Bytes (`bytes`), ByteArray (`bytearray`), MemoryView (`memoryview`)

### 8. None Type
- None (`None`)

## Examples

### String Data Type
```python
greet = 'welcome'  # String
castToString = str(3)

print(f"Type of greet is {type(greet)}")  # <class 'str'>
print(f"Type of castToString is {type(castToString)}")  # <class 'str'>
```

### Numeric Data Type
#### Integer
```python
currentYear = 2024  # int for year
print(f"Type of currentYear is {type(currentYear)}")  # <class 'int'>

castToInteger = int(2024.00)
print(f"Type of castToInteger is {type(castToInteger)}")  # <class 'int'>
```

#### Float
```python
weight = 75.50  # Float for weight in kg
print(f"Type of weight is {type(weight)}")  # <class 'float'>

castToFloat = float('75.50')
print(f"Type of castToFloat is {type(castToFloat)}")  # <class 'float'>
```

### Sequence Data Type
#### List
```python
fruits = ["apple", "banana", "cherry"]  # List for fruits
print(f"Type of fruits is {type(fruits)}")  # <class 'list'>

fruits.append("grapes")
print(f"Fruits List: {fruits}")  # ['apple', 'banana', 'cherry', 'grapes']
```

#### Tuple
```python
configuration = ('2MB', '30 Minutes')  # Tuple
print(f"Type of configuration is {type(configuration)}")  # <class 'tuple'>
print(f"Configuration Tuple: {configuration}")
```

### Mapping Data Type
#### Dictionary
```python
employeeDictionary = {"name": "John", "age": 36}  # Dict
print(f"Type of employeeDictionary is {type(employeeDictionary)}")  # <class 'dict'>
print(employeeDictionary)  # {'name': 'John', 'age': 36}

config = {True: "dummyValue", 1: "actualConfigValue"}  # Dict key conflict example
print(f"Config dictionary: {config}")  # {True: 'actualConfigValue'}
```

### Boolean Data Type
```python
eligibleToVote = True  # Boolean
print(f"Type of eligibleToVote is {type(eligibleToVote)}")  # <class 'bool'>
print(f"eligibleToVote: {eligibleToVote}")

sunRiseToday = 'east'
sunRiseTodayInWest = True if sunRiseToday == 'west' else False
print(f"Type of sunRiseTodayInWest is {type(sunRiseTodayInWest)}")  # <class 'bool'>
print(f"sunRiseTodayInWest: {sunRiseTodayInWest}")  # False
```

## TODO
- Add Bytes
- Add None examples

