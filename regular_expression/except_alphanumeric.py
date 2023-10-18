#except alphanumeric characters means specail characters

import re
word="Aa1! Bb2@ Cc#3 d"
result=re.finditer("[^a-zA-Z0-9]",word)
for i in result:
    print(i.start(),"----",i.end(),"----",i.group())
