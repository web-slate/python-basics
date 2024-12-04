def decimal_to_hexadecimal(decimal):
    hex_digits = "0123456789ABCDEF"
    hexadecimal = ""
    while decimal > 0:
        remainder = decimal % 16
        hexadecimal = hex_digits[remainder] + hexadecimal
        decimal //= 16
    return hexadecimal

decimal_number = int(input("Enter the number: "))  # For example: 76
hexadecimal_number = decimal_to_hexadecimal(decimal_number)
print(f"The hexadecimal equivalent of decimal {decimal_number} is {hexadecimal_number}.")
