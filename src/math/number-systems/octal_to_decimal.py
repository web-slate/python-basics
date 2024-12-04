def octal_to_decimal(octal):
    decimal = 0
    power = 0
    for digit in reversed(octal):  
        decimal += int(digit) * (8 ** power)
        power += 1
    return decimal


octal_number = input("Enter the octal number: ")    # For example: 56
decimal_number = octal_to_decimal(octal_number) 
print(f"The decimal equivalent of octal {octal_number} is {decimal_number}.")
