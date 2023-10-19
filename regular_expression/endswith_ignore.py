#to ignore the cases then we use the third parameter i.e,re.IGNORECASE
import re
word="iam working in thundersoft"
result=re.search("THUNDERSOFT$",word,re.IGNORECASE)
if result!=None:
    print("the string is ends with thundersoft")
else:
    print("the string is not ends with thundersoft")
