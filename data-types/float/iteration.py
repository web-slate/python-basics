print('\n >>>> Float Iteration Example')

mark = 78.80
weight = 68.50
height = 6.3
distance = 10.2
price = 27.50
latitude = 40.741895
longitude = -73.989308

print('\n >>>> Iterate using for loop with type casting to string')
print(' >>>> Follow this approach on demand and Its not recommended')
def iterateAfterTypeCasting(float_number):
    formatted_number = "{:.2f}".format(float_number)
    for text in formatted_number:
        print(text)

# iterateAfterTypeCasting(mark)
# iterateAfterTypeCasting(weight)
# iterateAfterTypeCasting(height)
# iterateAfterTypeCasting(distance)
# iterateAfterTypeCasting(price)
print('\n >>>> Iterate using while loop with operators')
number = 78.88

# Handle the integer part

# # Handle the fractional part
# fractional_part = (number - int(number))
# fractional_part = int((number - int(number)) * 100)
# rounded_fractional_part = round(fractional_part, 2)
# rounded_fractional_part_2 = int(fractional_part * 100 + 0.5) / 100.0

# print('fractional_part', fractional_part)
# print('rounded_fractional_part', rounded_fractional_part)
# print('rounded_fractional_part_2', rounded_fractional_part_2)

def iterateWithoutTypeCasting(float_number):
    int_part = int(float_number)
    stack = []
    while int_part > 0:
        digit = int_part % 10
        stack.append(digit)
        int_part //= 10
    
    while stack:
        print(stack.pop())


iterateWithoutTypeCasting(mark)
# iterateWithoutTypeCasting(weight)
# iterateWithoutTypeCasting(height)
# iterateWithoutTypeCasting(distance)
# iterateWithoutTypeCasting(price)
# iterateWithoutTypeCasting(latitude)

# print('\n >>>> Iterate using for loop with range')