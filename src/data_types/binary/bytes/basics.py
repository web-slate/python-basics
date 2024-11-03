# python module.py data_types/binary/bytes/basics.py
# python -m data_types.binary.bytes data_types/binary/bytes/basics.py
import sys
import os

# Add the parent directory of 'data_types' to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))

import data_types.commonUtils as utils

utils.print_h1('Byte Basics')

utils.print_blockquote([])