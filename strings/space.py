'''
Python String isspace() method returns “True” if all characters in the string are whitespace characters, Otherwise, It returns “False”. This function is used to check if the argument contains all whitespace characters, such as:

    ‘ ‘ – Space
    ‘\t’ – Horizontal tab
    ‘\n’ – Newline
    ‘\v’ – Vertical tab
    ‘\f’ – Feed
    ‘\r’ – Carriage return

Python String isspace() Method Syntax

    Syntax: string.isspace()

    Returns:

        True – If all characters in the string are whitespace characters.
        False – If the string contains 1 or more non-whitespace characters.

'''

str1="hello"
print(str1.isspace())

str1="hello hi123"
print(str1.isspace())

str2="hello \t hello"
print(str2.isspace())

str1="hello\nhi"
print(str1.isspace())

string="\n\t\n"
print(string.isspace())

