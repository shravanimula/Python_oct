'''
Python String isidentifier() method is used to check whether a string is a valid identifier or not. The method returns True if the string is a valid identifier, else returns False.
Python String isidentifier() method Syntax

    Syntax:  string.isidentifier()

    Parameters: The method does not take any parameters

'''
string="abcd_123"
print(string.isidentifier())

string="abcd 1234"
print(string.isidentifier())

str1="abcd"
print(str1.isidentifier())

str2=" abcd"
print(str2.isidentifier())


str3="abcd123"
print(str3.isidentifier())

str1="12345"
print(str1.isidentifier())

