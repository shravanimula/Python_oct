'''
^ Symbol:We can use ^ symbol to check whether the given target string starts with our provided pattern or not
'''

import re
word="iam working python and c "
result=re.search("^iam",word)
if result!=None:
    print("the string starts with iam")
else:
    print("the string not starts with iam")


word="iam working in thundersoft"
result=re.search("^thundersoft",word)
if result!=None:
    print("the string is starts with thundersoft")
else:
    print("the string is not starts with thundersoft")
