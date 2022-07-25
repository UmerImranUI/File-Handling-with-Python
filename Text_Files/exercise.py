def Displayforchar():

    f=open("DemoWrite.text","r")
    data=f.read()
    word=data.split()
    for i in word:
        if len(i)<7:
            print(i, end='\t')

Displayforchar()


def countupper():
    f=open("DemoWrite.text","r")
    count=0
    data=f.read()
    for i in data:
        if i.isupper():
            count+=1
    print("Total Upper Case Alphabets are: ", count)
    f.close()

countupper()