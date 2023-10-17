#example if the file is not there then 
'''
fd=open('demo.txt',"r")
print(fd.read())  

#FileNotFoundError: [Errno 2] No such file or directory: 'demo.txt'
'''
fd=open('demo.txt','r')
print(fd.read())
fd.close()


fd=open('demo.txt','r')
for word in fd:
    print(word)

fd.close()
