import re
word="hello iam  in thundersoft,iam in hyd"
result=re.search('iam',word)
if result!=None:
    print("match is available  the string and in the first occurance")
    print(result.start(),'---',result.end(),'----',result.group())

else:
    print("match is not available in  the string")

