import data_types.commonUtils as utils

utils.print_h1('1, 2 and 3 Bit Basics')

utils.print_h2('1 Bit')
print('''
| Decimal | Binary |
|---------|--------|
| 0       | 0      |
| 1       | 1      |
''')

utils.print_h2('2 Bit')
print('''
| Decimal | Binary |
|---------|--------|
| 0       | 00     |
| 1       | 01     |
| 2       | 10     |
| 3       | 11     |
''')

utils.print_h2('3 Bit')
print('In the 3-bit table, only decimal numbers up to 7 are included, as the binary representation of 8 (1000) requires 4 bits.')
print('''
| Decimal | Binary |
|---------|--------|
| 0       | 000    |
| 1       | 001    |
| 2       | 010    |
| 3       | 011    |
| 4       | 100    |
| 5       | 101    |
| 6       | 110    |
| 7       | 111    |
''')