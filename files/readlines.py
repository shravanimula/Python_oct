fd=open('demo.txt','r')
print(fd.readline()) #it will read one line
print(fd.readline())
fd.close()




with open('demo.txt','r') as fd:
    line=fd.readlines()
    for data in line:
        word=data.split()
        print(word)

fd.close()



fd=open('demo.txt','r')
for lines in fd:
    word=lines.split()
    print(word)

fd.close()
