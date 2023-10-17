#find the frequency of each character in string
def frequency_character(s):
    count_freq={}
    for i in s:
        if i in count_freq:
            count_freq[i]+=1
        else:
            count_freq[i]=1
    print("frequency of each character is:")
    print(count_freq)


string=input("enter a string:")
print("the string is:",string)
frequency_character(string)
