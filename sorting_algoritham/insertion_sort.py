def insertion_sort(a,n):
    for i in range(1,n):
        temp=a[i]
        j=i-1
        while(j>=0 and a[j]>temp):
            a[j+1]=a[j]
            j=j-1
        a[j+1]=temp
        
    return

array=[]
size=int(input("enter the size of the array:"))
print("enter the array elements are:\n")
for i in range(size):
    ele=int(input())
    array.append(ele)

print("before sorting the array is:")
for i in range(len(array)):
    print(array[i],end=' ')

insertion_sort(array,size)
print("\n after sorting the array is:")
for i in range(len(array)):
    print(array[i],end=' ')
