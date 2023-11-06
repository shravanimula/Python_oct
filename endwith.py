st1="hello good morning thundersoft"
st2='thundersoft'
print(st1.endswith(st2))

s1='hello go iam do in ho'
s2='o'
l1=[]
l1=s1.split()
l2=[]
for i in l1:
    if i.endswith(s2):
        l2.append(i)

print(l2)

print(' '.join(l2))
