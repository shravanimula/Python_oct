list1=[6,4,9,2,5,7,1]
print("before the sort the list:")
print(list1)
for i in range(len(list1)):
    for j in range(i+1,len(list1)):
        if(list1[i] > list1[j]):
            temp=list1[i]
            list1[i]=list1[j]
            list1[j]=temp

print("after sorting the list is:")
print(list1)
