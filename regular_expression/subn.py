'''
subn ():
It is exactly same as sub except it can also returns the number of replacements.
This function returns a tuple where first element is result string and second element is number of replacements.
'''

import re
target="iam in thundersoft and iam in hyd"
replacement="we"
regex="iam"
result=re.subn(regex,replacement,target)
print(result)
print("the result of string:",result[0])
print("the number of replacements:",result[1])

word="Aa1Bb2Cc3dD4"
result1=re.subn('[A-Z]',"*",word)
print(result1)
print("the result of string is :",result1[0])
print("the number of replacements is:",result1[1])

