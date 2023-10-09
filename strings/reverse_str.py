#reverse the string using slicing 
s="hello"
print("the original string:",s)
print("reverse the string is:",s[::-1])





#reverse the string using control statements
def reverse(s):
    rev=""
    for i in s:
        rev=i+rev
    return rev


str="hello this is python"
print("the original string is:",str)
print(reverse(str))





#reverse the sting using recursion
def revers(s):
    if len(s) == 0:
        return s
    else:
        return revers(s[1:]) + s[0]


s1="reversefunction"
print("original string:",s1)
print(revers(s1))
