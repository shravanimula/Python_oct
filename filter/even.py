'''
Filter ():
• This function is used to filter the values from given sequence based on
condition.
• syntax: filter(function, sequence)
• here first parameter function is for conditional check
• here second parameter sequence can be a list or tuple or set
'''

def even(a):
    if a%2==0:
        return True
    else:
        return False

list1=[11,22,33,44,55,66,77,88]
list2=list(filter(even,list1))
print(list2)
