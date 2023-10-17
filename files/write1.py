fd=open('text.txt','w')

for i in range(4):
    name=input("enter name:")
    fd.write(name)
    fd.write("\n")

fd.close()

fd=open('text.txt','r')
for word in fd:
    print(word)
fd.close()
