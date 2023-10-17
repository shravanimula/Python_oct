'''
i have already demo1 file is there in that file only iam writting
the data will be over written happen
'''

fd=open('demo1.txt','w')
fd.write('file concept in python')
fd.close()

fd=open('demo1.txt','r')
print(fd.read())
fd.close()
