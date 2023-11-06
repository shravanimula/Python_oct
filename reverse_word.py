#to reverse the word in a string

st1=input("enter a string:")
word=st1.split()[::-1]

l=[]
for i in word:
    l.append(i)

print(' '.join(l))



