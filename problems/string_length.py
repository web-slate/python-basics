print('\n >>> String Length Example without using len() def')
print(' >>> string_length()')
def string_length(text):
    count = 0;
    for character in text:
        count += 1
    
    return count;


print("string_length('Venkat'): ", string_length('Venkat'))
print("string_length(R.Venkat): ", string_length('R.Venkat'))
print("string_length('Python'): ", string_length('Python'))
print("string_length('Full Stack Development'): ", string_length('Full Stack Development'))
print("string_length(734250): ", string_length(734250))
print("string_length(52734250): ", string_length(52734250))