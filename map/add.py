'''
Map ():
• for every element present in sequence, apply some condition and
Return the new sequence of elements for this purpose we use map
function.
• syntax: filter(function, sequence)
• here first parameter function is for conditional check
• here second parameter sequence can be a list or tuple or set
'''

def addition(a):
    return a+a

list1=[1,2,3,4,5,6]
result=tuple(map(addition,list1))
print(result)
