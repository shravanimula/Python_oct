fd=open('demo.txt','a')
fd.write('adding new line')
fd.close()

fd=open('demo.txt','r')
print(fd.read())
fd.close()
