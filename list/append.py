a=[11,22,33,44]
print(a)
a.append(55)
print(a)


list1=[]
n=int(input("enter the range of list:"))
print("enter the list elements:")
for i in range(0,n):
    element=int(input())
    list1.append(element)

print("the list elements are:")
print(list1)
