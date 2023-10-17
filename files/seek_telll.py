'''
tell(): We can use tell() method to return current position of the
cursor (file pointer) from beginning of the file.
Seek() : We can use seek() method to move cursor(file pointer) to
specified location
'''

fp=open('demo.txt','r')
print(fp.tell())
print(fp.read(8))
print(fp.seek(2))
print(fp.tell())
print(fp.seek(3))
print(fp.read(4))
print(fp.tell())
