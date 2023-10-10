list1=[1,2,3,4,56]
print("before reverse list:",list1)
print("after reverse list:",list1[::-1])

rev_list=[]
print("before reverse:",list1)
for i in list1:
    rev_list=[i]+rev_list

print("reverse list:",rev_list)

list2=[]
for i in range(len(list1)):
    list2.append(list1.pop())

print("the list2 is:",list2)

