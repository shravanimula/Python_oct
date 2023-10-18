#compile () : This function is used to compile a pattern into Regex Object.
'''
finditer(): Returns an Iterator object which , Match object for every Match
 On Match object we can call the following methods.
 start() : Returns start index of the match
 end() : Returns end+1 index of the match
group() : Returns the matched string
'''

import re
word="abcdabefghab"
pattern=re.compile('ab')
result=re.match(pattern,word)
print(result)
