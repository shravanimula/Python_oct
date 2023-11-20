def selection_sort(a,n):
    for i in range(n):
        min=i
        for j in range(i+1,n):
            if (a[min] > a[j]):
                min=j

        a[i],a[min]=a[min],a[i]
    return


array=[]
size=int(input("enter rthe size of the array:"))
print("enter the array elements are:")
for i in range(size):
    ele=int(input())
    array.append(ele)

print("before sorting the array elements are:")
for i in range(len(array)):
    print(array[i],end=' ')

selection_sort(array,size)
print("\n after sorting elements are:")
for i in range(len(array)):
    print(array[i],end=' ')
