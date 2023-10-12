'''
Reduce ():
• Reduce () function reduces sequence of elements into a single element by
applying the specified function.
• syntax: filter(function, sequence)
• Reduce () function present in functools module and hence we should write
import statement.
'''

from functools import reduce
def add(a,b):
    return a+b

list1=[1,2,3,4,5,]
result=reduce(add,list1)
print(result)
