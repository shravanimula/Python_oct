#finditer(): Returns an Iterator object which , Match object for every Match

import re
word="abcdabefab"
pattern="ab"
match1=re.finditer(pattern,word)
for i in match1:
    print(i.start(),'---',i.end(),'----',i.group())
