with open('demo2.txt','w') as fd:
    fd.write('hello this is new file')
    fd.write('python file')

fd.close()

fd=open('demo2.txt','r')
print(fd.read())
fd.close()
