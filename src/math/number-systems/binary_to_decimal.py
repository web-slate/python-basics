def binary_to_decimal(binary):
    decimal = 0
    power = 0
    for digit in reversed(binary):  # Process digits from right to left
        decimal += int(digit) * (2 ** power)
        power += 1
    return decimal


binary=input("Enter the binary:")   # For example: 1011
decimal = binary_to_decimal(binary)
print(f"The decimal equivalent of binary {binary} is {decimal}")