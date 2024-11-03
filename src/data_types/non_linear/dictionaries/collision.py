# python module.py data_types/dictionaries/collision.py
# python -m data_types.dictionaries.collision data_types/dictionaries/collision.py

import data_types.commonUtils as utils

utils.print_h1('Hashing Basics')
utils.print_ordered_list([
    'Hashing concepts have been around since the 1950s and cryptography became prominent in the 1970s.'
    'Process of converting an input (of any length) into a fixed-size string of bytes.',
    'Typically for the purpose of security, indexing, or identification.',
    'Output is known as a hash value or hash code.'
    'Used for Data Retrieval in Hash Map / Dictionary, ',
    'Used for Cryptography Security, hashing creates almost-unique identifiers for data for password storage, digital signatures, and message integrity checks',
    'Used for Caching to identify data with unique hash values',
    'Used for Load Balancing, consistent hashing helps in evenly distributing the load.'
])

utils.print_h2('Collision in')
utils.print_ordered_list([
    'Even Modern programming languages use sophisticated hashing algorithms but collisions can still occur.',
    'According to the Pigeonhole Principle, collisions (where different keys produce the same hash value) are inevitable.',
    'Efficiency of a hashing algorithm lies in minimizing these collisions and dealing with them effectively when they occur.'
])

print('''
| Language   | Hashing Algorithm           |
|------------|-----------------------------|
| Python     | SipHash                     |
| Java       | Object.hashCode() method (varies based on object; often a variation of DJB2) |
| JavaScript | V8 (Chrome, Node.js): One-at-a-time (variations) |
|            | SpiderMonkey (Firefox): DJB2 (variations) |
|            | JavaScriptCore (Safari): Engine-specific implementation |
| C#         | .NET Framework: Marvin32 (with modifications) |
| Go         | AEAD (AES-GCM) based algorithm |

''');

alamelu.gotara@gmail.com
Code@2050
alamelu-gotara