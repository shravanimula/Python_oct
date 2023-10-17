#read file using with statements

with open('demo.txt') as fd:
    word=fd.read()

print(word)

