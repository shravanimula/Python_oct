'''
$ Symbol:We can use $ symbol to check whether the given target string ends with our provided pattern or not
'''

import re
word="iam working python and c "
result=re.search("python$",word)
if result!=None:
    print("the string ends with python")
else:
    print("the string is not ends with python")


word="iam working in thundersoft"
result=re.search("thundersoft$",word)
if result!=None:
    print("the string is ends with thundersoft")
else:
    print("the string is not ends with thundersoft")
