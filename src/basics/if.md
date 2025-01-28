# Statement Example

## isEligibleToVote Function with Passing Age

This section demonstrates a simple function to check if someone is eligible to vote based on their age.

### Function Definition
```python
def isEligibleToVote(age: int = 0) -> None:
    try:
        if age > 0 and age < 21:
            print(str(age) + ' Wow, You will be soon eligible to vote')
        elif age > 21:
            print(str(age) + ' Congrats, You are eligible to vote!')
        else:
            print(str(age) + ' Invalid `age` parameter')
    except Exception as e:
        print('Got error for param "' + age + '"\nError is ', e)
```

### Example Usage

#### Passing Nothing (Default Parameter)
By default, if no parameter is passed, the default value of `age = 0` is used.
```python
isEligibleToVote()
```
**Output:**
```
0 Invalid `age` parameter
```

#### Passing `16` as Parameter
```python
isEligibleToVote(16)
```
**Output:**
```
16 Wow, You will be soon eligible to vote
```

#### Passing `19` as Parameter
```python
isEligibleToVote(19)
```
**Output:**
```
19 Wow, You will be soon eligible to vote
```

#### Passing `25` as Parameter
```python
isEligibleToVote(25)
```
**Output:**
```
25 Congrats, You are eligible to vote!
```

#### Passing Empty String as Parameter
When passing an empty string, it throws a `TypeError` because comparison between a string and an integer is not supported.
```python
isEligibleToVote('')
```
**Output:**
```
Got error for param ""
Error is  '<' not supported between instances of 'str' and 'int'
```

