print('\n >>>> Integer Iteration Example')

salary = 9000
increment = 500

print('\n >>>> Iterate using for loop with type casting')
print(' >>>> Follow this approach on demand and Its not recommended')
for text in str(salary):
    print(text)
    
print('\n >>>> Iterate using while loop')
stack = []

while salary > 0:
    digit = salary % 10
    stack.append(digit)
    salary //= 10

while stack:
    print(stack.pop())
