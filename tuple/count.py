tuple1=(1,2,3,4,2,6,2,3,4)
print(tuple1)
count=0
element=2
for i in tuple1:
    if(i==element):
        count=count+1

print("The number of occurance of {} is:{}".format(element,count))
