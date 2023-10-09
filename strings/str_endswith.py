string = "hello python"
print(string.endswith("python"))

s1="hi hello abhi vani raju"
l=s1.split() #split the string
list1=[]
for i in l:
    if i.endswith('i'):  #if condition true
        list1.append(i) # adding to the list

print(list1)
#list elements storing  into string 
s1=' '.join(list1)
print(s1)

