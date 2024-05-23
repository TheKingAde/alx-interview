#!/usr/bin/python3
"""
UTF8 validator
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Parameters:
    data (List[int]): A list of integers where each integer represents a byte.

    Returns:
    bool: True if data is a valid UTF-8 encoding, else False.
    """

    # Number of bytes in the current UTF-8 character
    number_of_bytes = 0

    # Masks to check the first byte of a character
    mask1 = 1 << 7
    mask2 = 1 << 6

    # Iterate through each byte in the data
    for byte in data:
        # Get only the last 8 bits of the integer
        byte = byte & 0xFF

        if number_of_bytes == 0:
            # Determine the number of bytes for the UTF-8 character
            mask = 1 << 7
            while mask & byte:
                number_of_bytes += 1
                mask = mask >> 1

            # If number_of_bytes is 0, it's a 1-byte character
            if number_of_bytes == 0:
                continue

            # If the number of bytes is greater than 4 or 1, return False
            if number_of_bytes == 1 or number_of_bytes > 4:
                return False

        else:
            # Else, it's a continuation byte and must start with '10xxxxxx'
            if not (byte & mask1 and not (byte & mask2)):
                return False

        # Decrease the number of bytes to check for the current character
        number_of_bytes -= 1

    # If number_of_bytes is not 0, the last character was not complete
    return number_of_bytes == 0
