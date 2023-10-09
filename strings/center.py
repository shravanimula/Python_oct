'''
Python String center() method creates and returns a new string that is padded with the specified character.

    Syntax:  string.center(length[, fillchar])

    Parameters:

        length: length of the string after padding with the characters.
        fillchar: (optional) characters which need to be padded. If it’s not provided, space is taken as the default argument.

    Returns: Returns a string padded with specified fillchar and it doesn’t modify the original string.
'''

s="new python code"
new_string = s.center(28, '*')
print("After padding String is:", new_string)

