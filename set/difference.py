'''
A - B is equal to the elements present in A but not in B
B - A is equal to the elements present in B but not in A
set_A.difference(set_B) for (A - B)
set_B.difference(set_A) for (B - A)
'''
set1={10,20,30,40,100}
set2={100,200,300,20}
print("set1:",set1)
print("set2:",set2)
print("difference of set1-set2 is:",set1-set2)

print("difference of set2-set1 is:",set2-set1)

print("set1-set2:",set1.difference(set2))
print("set2-set1:",set2.difference(set1))


