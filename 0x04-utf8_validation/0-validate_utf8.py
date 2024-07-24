#!/usr/bin/python3
"""Modeule for UTF-8 Validation Module"""


def validUTF8(data):
    """
    Function determines if a given data set represents a valid
    UTF-8 encoding.
    """
    numberBytes = 0

    mask1 = 1 << 7
    mask2 = 1 << 6

    for i in data:

        maskBytes = 1 << 7

        if numberBytes == 0:

            while maskBytes & i:
                numberBytes += 1
                maskBytes = maskBytes >> 1

            if numberBytes == 0:
                continue

            if numberBytes == 1 or numberBytes > 4:
                return False

        else:
            if not (i & mask1 and not (i & mask2)):
                    return False

        numberBytes -= 1

    if numberBytes == 0:
        return True

    return False
