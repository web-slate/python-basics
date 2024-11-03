# python module.py data_types/binary/bytearray/basics.py
# python -m data_types.binary.bytearray data_types/binary/bytearray/basics.py
import sys
import os

# Add the parent directory of 'data_types' to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))

from data_types import commonUtils as utils

utils.print_h1('Byte Array Basics')

utils.print_blockquote([])