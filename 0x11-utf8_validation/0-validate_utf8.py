#!/usr/bin/python3
""" method that determines if a given
data set represents a valid UTF-8 encoding.
"""


import sys
# - A valid UTF-8 character can be 1 - 4 bytes long.
# - For a 1-byte character, the first bit is a 0, followed
# by its unicode.
# - For an n-bytes character, the first n-bits are all ones,
# the n+1 bit is 0, followed by n-1 bytes with most significant
# 2 bits being 10.
# - The input given would be an array of integers containing
# the data. We have to return if the data in the array represents
# a valid UTF-8 encoding. The important thing to note here
# is that the array doesn't contain data for just a single
# character. As can be seen from the first example, the
# array can contain data for multiple characters all of
# which can be valid UTF-8 characters and hence the charset
# represented by the array is valid.Another important thing
# to note is that the integers in the array can be larger
# than 255 as well. The highest number that can be represented
# by 8 bits is 255. So, what do we do if an integer in the
# array is say, 476? According to the Note in the problem before
# the examples, we only have to consider the 8 least significant
# bits of each integer in the array.


def validUTF8(data):
    """
    :type data: List[int]
    :rtype: bool
    """

    # Number of bytes in the current UTF-8 character
    n_bytes = 0

    # For each integer in the data array.
    for num in data:

        # Get the binary representation. We only need the least significant 8
        # bits for any given number.
        bin_rep = format(num, '#010b')[-8:]

        # If this is the case then we are to start processing a new UTF-8
        # character.
        if n_bytes == 0:

            # Get the number of 1s in the beginning of the string.
            for bit in bin_rep:
                if bit == '0':
                    break
                n_bytes += 1

            # 1 byte characters
            if n_bytes == 0:
                continue

            # Invalid scenarios according to the rules of the problem.
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            # Else, we are processing integers which represent bytes which are
            # a part of a UTF-8 character. So, they must adhere to the pattern
            # `10xxxxxx`.
            if not (bin_rep[0] == '1' and bin_rep[1] == '0'):
                return False

        # We reduce the number of bytes to process by 1 after each integer.
        n_bytes -= 1

    # This is for the case where we might not have the complete data for
    # a particular UTF-8 character.
    return n_bytes == 0
