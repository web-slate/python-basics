def roman_to_decimal(roman):
    # Define Roman numeral to decimal mappings
    roman_to_decimal_map = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    decimal = 0
    prev_value = 0

    # Iterate through each Roman numeral in reverse order
    for numeral in reversed(roman):
        value = roman_to_decimal_map[numeral]
        
        # Subtract if the value is less than the previous value, otherwise add
        if value < prev_value:
            decimal -= value
        else:
            decimal += value

        prev_value = value  # Update the previous value

    return decimal


roman_number = input("Enter the Roman numeral: ").upper()    # for example MCMLXXXVII
try:
    decimal_number = roman_to_decimal(roman_number)
    print(f"The decimal equivalent of Roman numeral {roman_number} is {decimal_number}.")
except KeyError:
    print("Invalid Roman numeral. Please enter a valid Roman numeral.")
