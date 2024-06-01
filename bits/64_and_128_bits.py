from stylepy import h1, h2, h3, h4, h5, h6

h1('64 and 128 Bit Basics')

h2('64 Bits')
print('Note: 64 bits can represent numbers from 0 to 18,446,744,073,709,551,615 (2^64 - 1). Only the least significant 16 bits are shown.')
print('''
| Decimal | Binary (only showing least significant 16 bits for brevity) |
|---------|------------------------------------------------------------|
| 0       | 0000000000000000                                           |
| 1       | 0000000000000001                                           |
| 2       | 0000000000000010                                           |
| ...     | ...                                                        |
| 10      | 0000000000001010                                           |
''')

h2('128 Bits')
print('Note: 128 bits can represent a very large range of numbers, from 0 up to 340,282,366,920,938,463,463,374,607,431,768,211,455 (2^128 - 1). Only the least significant 16 bits are shown for simplicity.')
print('''
| Decimal | Binary (only showing least significant 16 bits for brevity) |
|---------|------------------------------------------------------------|
| 0       | 0000000000000000                                           |
| 1       | 0000000000000001                                           |
| 2       | 0000000000000010                                           |
| ...     | ...                                                        |
| 10      | 0000000000001010                                           |
''')