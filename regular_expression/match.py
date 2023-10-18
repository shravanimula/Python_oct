'''
match ():
We can use match function to check the given pattern at beginning of target string.
If the match is available then we will get Match object, otherwise we will get None.
'''
import re
word="hello iam  in thundersoft"
result=re.match('in',word)
if result!=None:
    print("match is available  at beginnnig of the string")
    print(result.start(),'---',result.end(),'----',result.group())

else:
    print("match is not available at the beginnig of the string")



word1="hello iam  in thundersoft"
result=re.match('hello',word1)
if result!=None:
    print("match is available  at beginnnig of the string")
    print(result.start(),'---',result.end(),'----',result.group())

else:
    print("match is not available at the beginnig of the string")

