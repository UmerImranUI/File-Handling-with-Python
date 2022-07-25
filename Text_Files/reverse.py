
a=input("enter the word: ")
word=[]
b=len(a)
b-=1
for i in a:
    word.append(a[b])
    b-=1
word1=''.join(word)
if a==word1:
    print("This word is palendrome: ",word1)
else:
    print("no")


