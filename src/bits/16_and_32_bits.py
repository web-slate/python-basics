from stylepy import h1, h2, h3, h4, h5, h6

h1('16 and 32 Bit Basics')

h2('16 Bits')
h4('Note: 16 bits can represent numbers from 0 to 65,535 (2^16 - 1).')
h4('''
| Decimal | Binary            |
|---------|-------------------|
| 0       | 0000000000000000  |
| 1       | 0000000000000001  |
| 2       | 0000000000000010  |
| 3       | 0000000000000011  |
| 4       | 0000000000000100  |
| 5       | 0000000000000101  |
| 6       | 0000000000000110  |
| 7       | 0000000000000111  |
| 8       | 0000000000001000  |
| 9       | 0000000000001001  |
| 10      | 0000000000001010  |
''')

h2('32 Bits')
h4('Note: 32 bits can represent numbers from 0 to 4,294,967,295 (2^32 - 1). Full binary representation for numbers larger than 16 bits is quite lengthy, so only the least significant 16 bits are shown for brevity.')
h4('''
| Decimal | Binary (only showing least significant 16 bits for brevity) |
|---------|------------------------------------------------------------|
| 0       | 0000000000000000                                           |
| 1       | 0000000000000001                                           |
| 2       | 0000000000000010                                           |
| ...     | ...                                                        |
| 10      | 0000000000001010                                           |
''')