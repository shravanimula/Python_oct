def binarysearch(a,low,high,ele):
    if(high >= low):
        mid=(high+low)//2
        if(a[mid]==ele):
            return mid
        elif a[mid] > ele:
            return binarysearch(a,low,mid-1,ele)
        else:
            return binarysearch(a,mid+1,high,ele)

    else:
        return -1


array=[]
size=int(input("enter the size of array:"))
print("enter the array elements are:")
for i in range(size):
    ele=int(input())
    array.append(ele)
print("the array elements are:")
for i in range(size):
    print(array[i],end=' ')

element=int(input("\nenter the element to search:"))
result=binarysearch(array,0,len(array)-1,element)
if(result==-1):
    print("element is not found in the array index")
else:
    print(" element is found in the array index is :",result)

