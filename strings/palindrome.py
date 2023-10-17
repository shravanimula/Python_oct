def palindrome(s):
    length=len(s)
    for i in range(0,length//2):
        if s[i] != s[length-i-1]:
            return False
    return True


string=input("enter a string:")
result=palindrome(string)
if result==1:
    print('given string is palindrome:',string)
else:
    print('given string is not palindrome:',string)
