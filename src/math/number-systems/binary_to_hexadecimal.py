def binary_to_hexadecimal(binary):
    # Binary to hexadecimal mapping
    binary_to_hex = {
        "0000": "0", "0001": "1", "0010": "2", "0011": "3",
        "0100": "4", "0101": "5", "0110": "6", "0111": "7",
        "1000": "8", "1001": "9", "1010": "A", "1011": "B",
        "1100": "C", "1101": "D", "1110": "E", "1111": "F"
    }
    
    # Pad binary to make its length a multiple of 4
    while len(binary) % 4 != 0:
        binary = "0" + binary
    
    # Convert groups of 4 to hexadecimal
    hexadecimal = ""
    for i in range(0, len(binary), 4):
        group = binary[i:i+4]
        hexadecimal += binary_to_hex[group]
    
    return hexadecimal

binary_number = input("Enter the binary number: ")   # For example 1011 or 0001
hexadecimal_number = binary_to_hexadecimal(binary_number)
print(f"The hexadecimal equivalent of binary {binary_number} is {hexadecimal_number}.")
