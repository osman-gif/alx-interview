#!/usr/bin/python3
"""
Write a method that determines if a given data set represents a valid
UTF-8 encoding.

    Prototype: def validUTF8(data)
    Return: True if data is a valid UTF-8 encoding, else return False
    A character in UTF-8 can be 1 to 4 bytes long
    The data set can contain multiple characters
    The data will be represented by a list of integers
    Each integer represents 1 byte of data, therefore you only need to
    handle the 8 least significant bits of each integer
"""


def validUTF8(data):
    """Check if a list of integers represents a valid UTF-8 encoding"""

    n_bytes = 0
    for num in data:
        mask = 1 << 7
        if not n_bytes:
            while mask & num:
                n_bytes += 1
                mask = mask >> 1
            if not n_bytes:
                continue
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            if not (num & 1 << 7 and not num & 1 << 6):
                return False
        n_bytes -= 1
    return n_bytes == 0
