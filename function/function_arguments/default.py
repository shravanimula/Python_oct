'''
function accepts atleast one default value
if a value is passed to default argument,the default value gets replaced with the new value
'''

def default(m,n,o,p=1):
    print("m={} n={} o={}  p={} ".format(m,n,o,p))


default(10,20,30)
default("aaa","bbb","ccc","ddd")
default(1.2,4.8,11,22)
default("aa",1,.22)
