from stylepy import h1, h2, h3, h4, h5, h6
from stylepy import ordered_list, bullet_list

h1('Data Type Bit Sizes')

print('''
| Data Type  | Typical Maximum Bits       | Notes                                           |
|------------|----------------------------|-------------------------------------------------|
| int        | Variable (system-dependent)| Limited by available memory, can be very large. |
| float      | 64                         | Double-precision float, IEEE 754 standard.      |
| complex    | 2x64                       | Consists of two 64-bit floats.                  |
| bool       | 8                          | Typically stored as a byte.                     |
| str        | Variable (system-dependent)| Dependent on length and encoding.               |
| bytes      | Variable (system-dependent)| Dependent on the length of the sequence.        |
| bytearray  | Variable (system-dependent)| Similar to bytes, mutable version.              |
| list       | Variable (system-dependent)| Dependent on the number and types of elements.  |
| tuple      | Variable (system-dependent)| Dependent on the number and types of elements.  |
| set        | Variable (system-dependent)| Dependent on the number of elements.            |
| dict       | Variable (system-dependent)| Dependent on the number of key-value pairs.     |
| NoneType   | N/A                        | Represents no value, no associated bit size.    |
''')

h2('Notes')
ordered_list(
    [
        'The "int" type in Python can handle very large numbers, as its size is dynamic and adjusts based on the value it\'s holding.',
        'For types like "str", "bytes", "bytearray", "list", "tuple", "set", and "dict", the bit size depends on their content and can vary widely.',
        '"NoneType" does not represent a data storage type and thus does not have an associated bit size.',
        'The sizes for "float" and "complex" are more standardized due to the use of the IEEE 754 standard for floating-point arithmetic.',
    ]
)
