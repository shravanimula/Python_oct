list1=[2,3,4,5,6,7,8]

print("even numbers")
result=filter(lambda a:a%2==0,list1)
list2=list(result)
print(list2)

print("odd numbers")
result=list(filter(lambda b:b%2!=0,list1))
print(result)
