'''
pop():removes the item with the key and returns its value or .if key is not found it raises keyerror.
'''

Dict={1:'aaa',2:'bbb',3:'cccc',4:'dddddd'}
print(Dict)
a=Dict.pop(3)
print(a)

#popitem():removes and returns an arbitrary item(key,value).raises keyerror if the dictionary is empty

Dict1={1:'one',2:'two',3:'three',4:'four'}
print(Dict1)

print("pop item is:",Dict1.popitem())
print(Dict1)
