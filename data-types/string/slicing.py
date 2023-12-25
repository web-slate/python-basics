print('\n >>>> String Slicing Example')
print('s[start:end] extracts the substring from index start to end - 1.')
print('s[start:end:step] extracts the substring from index start to end - 1')

greet = "welcome"
debit_card = "1234-5678-9012-3456"
slicing_detailed_desc = '''In Python, slicing a string, list, or any other sequence type is a very efficient operation in terms of time complexity. Here's a brief overview:
Time Complexity: O(k)
Space Complexity:: O(k)
'''
tutorial_site = 'https://webslate.io/blogs/algorithms/big-o-notations'
email_id = 'username@example.com'
phone_number = '+1-800-555-1234'
file_name = 'slicing.pdf'
transaction_timestamp = '2023-01-15 09:30:00'

print('\n >>>> Get last four digit of debit card', '[-4:]')
print(debit_card[-4:])

print('\n >>>> Get short description from long string', '[:140]')
print(slicing_detailed_desc[:140], '...')

print('\n >>>> Get Mobile Country and Area Code', '[0:6]')
print(phone_number[0:6])

print('\n >>>> Get File extension', '[-3]')
print(file_name[-3:])

print('\n >>>> Get Transaction Date', '[0:10]')
print(transaction_timestamp[0:10])

print('\n >>>> Get Transaction Year', '[0:4]')
print(transaction_timestamp[0:4])

print('\n >>>> Get Transaction Month', '[5:7]')
print(transaction_timestamp[5:7])

print('\n >>>> Get Transaction Time with seconds', '[-8:]')
print(transaction_timestamp[-8:])

print('\n >>>> Get Transaction hour in Time without seconds', '[-8:-3]')
print(transaction_timestamp[-8:-3])

print('\n >>>> Get Time String Revered', '[::-1]')
print(transaction_timestamp[::-1])

