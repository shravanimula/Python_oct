'''
split ():
If we want to split the given target string according to a particular pattern then we should go for split() function.This function returns list of all tokens.
'''

import re
string="iam in thundersoft and iam in hyd"
result=re.split("\s",string)
print(result)
