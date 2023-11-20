def linearsearch(a,size,key): 
    for i in range(0,size):
        if (a[i] == key):
            return i
    return -1

array=[]
n=int(input("enter the size of array:"))

print("enter the array elements:")
for i in range(n):
    element=int(input())
    array.append(element)

print("the array elements are:")
for i in range(n):
    print(array[i],end=" ")

ele=int(input("\nenter a elemnts to search:"))

result=linearsearch(array,n,ele)
if (result == -1):
    print("element is not present in the array")
else:
    print("element is present in the array index is",result)
