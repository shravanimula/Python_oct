def function(characters):
    letters = ['a', 'e', 'i', 'o', 'u']
    if(characters in letters):
        return True
    else:
        return False
 
 
string1=['h','e','l','o','u', 'a','r','u']
list2=list(filter(function,string1))
print('the letters are:')
for i in list2:
    print(i)
