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

hashing_algorithm_by_languages = [
    ("Java", "Java's HashMap uses a variant of hashing with chaining for collision resolution.",
     "O(1) for get/put operations", "O(n)"),
    ("Scala", "Scala's standard library collections use similar approaches to Java, often built on top of Java's collections.",
     "O(1) for get/put operations", "O(n)"),
    ("Python", "Python's dictionaries use a combination of open addressing and random probing.",
     "O(1) for access/search/insert/delete", "O(n)"),
    ("Node.js", "In JavaScript (Node.js), objects and Maps use similar hashing techniques with chaining.",
     "O(1) for access/search/insert/delete", "O(n)"),
    (".NET", ".NET's Dictionary class uses a version of chaining for collision resolution.",
     "O(1) for get/put operations", "O(n)")
]
