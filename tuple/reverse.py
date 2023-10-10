tuple1=(11,22,33,44,55,66)
print(tuple1)
list1=list(tuple1)
rev=[]
for i in list1:
    rev=[i]+rev

tuple1=tuple(rev)
print("reverse of the tuple is:")
print(tuple1)

