#import data_types.commonUtils as utils
from stylepy import h1, h2, h3, h4, h5, h6

h1('1, 2 and 3 Bit Basics')

h2('1 Bit')
h6('''
| Decimal | Binary |
|---------|--------|
| 0       | 0      |
| 1       | 1      |
''')

h2('2 Bit')
h4('''
| Decimal | Binary |
|---------|--------|
| 0       | 00     |
| 1       | 01     |
| 2       | 10     |
| 3       | 11     |
''')

h2('3 Bit')
h4('In the 3-bit table, only decimal numbers up to 7 are included, as the binary representation of 8 (1000) requires 4 bits.')
h4('''
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