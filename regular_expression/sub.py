'''
sub ():
sub means substitution or replacement
re.sub(regex,replacement,targetstring)
In the target string every matched pattern will be replaced with provided replacement.
'''

import re
target="iam in thundersoft and iam in hyd"
replacement="we"
regex="iam"
result=re.sub(regex,replacement,target)
print(result)

word="Aa1Bb2CC3dD4"
result=re.sub('[A-Z]',"*",word)
print(result)
