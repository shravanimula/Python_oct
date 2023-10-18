import re
word="Aa1Bb2Cc3"
match1=re.finditer('[a-z]',word)
for i in match1:
    print(i.start(),'---',i.end(),'----',i.group())
