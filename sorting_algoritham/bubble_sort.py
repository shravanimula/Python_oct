def bubble_sort(a,n):
    for i in range(n):
        for j in range(0,n-i-1):
            if (a[j] > a[j+1]):
                a[j],a[j+1]=a[j+1],a[j]

    return


array=[]
n=int(input("enter the size of array:"))
for i in range(n):
    ele=int(input())
    array.append(ele)

print("before sorting the array is:")
for i in range(len(array)):
    print(array[i],end=" ")

bubble_sort(array,n)

print("\nafter sorting the array is:")
for i in range(len(array)):
    print(array[i],end=' ' )

