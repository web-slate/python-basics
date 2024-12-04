def decimal_to_binary(decimal):
    binary = ""
    while decimal > 0:
        remainder = decimal % 2
        binary = str(remainder) + binary
        decimal //= 2
    return binary


decimal_number = int(input("Enter the decimal number: "))  # for example : 10

binary_number = decimal_to_binary(decimal_number)

print(f"The binary equivalent of decimal {decimal_number} is {binary_number}.")
