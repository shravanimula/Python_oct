#updates the dictionary with the key/value pairs from other,overwirting existing keys
a={1:'aa',2:'bbb',3:'ccc'}
print("a dict:",a)
b={4:'ddd',5:'eee'}
print("b dict:",b)
a.update(b)
print("update dict:",a)
