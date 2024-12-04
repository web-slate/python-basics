def hexadecimal_to_decimal(hexadecimal):
    hex_digits = "0123456789ABCDEF"
    decimal = 0
    power = 0
    for digit in reversed(hexadecimal.upper()): 
        decimal += hex_digits.index(digit) * (16 ** power)
        power += 1
    return decimal


hexadecimal_number=input("Enter the hexadecimal_number:")      # For example:  1A
decimal_number = hexadecimal_to_decimal(hexadecimal_number)
print(f"The decimal equivalent of hexadecimal {hexadecimal_number} is {decimal_number}.")
