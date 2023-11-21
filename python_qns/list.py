'''
We call append() method to add an item to the end of a list.
We call extend() method to add another list to the end of a list.
In append() we have to add items one by one. But in extend() multiple items
from another list can be added at the same time.
'''

list1=[]
n=int(input("enter the range of list:"))
print("enter the list elements:")
for i in range(0,n):
    element=int(input())
    list1.append(element)

print("the list elements are:")
print(list1)



list1=[11,22,33]
print("initial list:",list1)
list1.extend(["aaa","bbb","ccc"])
print("after extend the list was:")
print(list1)
