def decimal_to_octal(decimal):
    octal = ""
    while decimal > 0:
        remainder = decimal % 8
        octal = str(remainder) + octal
        decimal //= 8
    return octal


decimal_number = int(input("Enter the decimal number: "))   # for example 26
octal_number = decimal_to_octal(decimal_number)
print(f"The octal equivalent of decimal {decimal_number} is {octal_number}.")