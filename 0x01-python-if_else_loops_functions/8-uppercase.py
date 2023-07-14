#!/usr/bin/python3
def uppercase(str):
    """Function to convert uppercase characters to lowercase"""

    new_string = ""
    for element in str:
        element = ord(element)
        if (element >= 97) and element <= 122:
            element -= 32
        new_string += chr(element)
    print(new_string)
