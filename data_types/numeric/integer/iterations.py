# print('\n >>>> Integer Iteration Example')

# salary = 9000
# increment = 500

print('\n >>>> Iterate using for loop with type casting')
# print(' >>>> Follow this approach on demand and Its not recommended')
# for text in str(salary):
#     print(text)
    
# print('\n >>>> Iterate using while loop')
# def iterateInteger(integer_number):
#     stack = []
#     while integer_number > 0:
#         digit = integer_number % 10
#         stack.append(digit)
#         integer_number //= 10
    
#     while stack:
#         print(stack.pop())
            
# iterateInteger(salary)

def iterateInteger(integer_number):
    stack = []
    while integer_number > 0:
        digit = integer_number % 10
        stack.append(digit)
        integer_number //= 10
    
    while stack:
        print(stack.pop())