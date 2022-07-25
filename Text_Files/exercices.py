def countEndT():
    f=open("DemoWrite.txt")
    count=0
    data=f.read()
    words=data.split()
    for i in words:
        if i[-1]=='t':
            count+=1
            print(i)
    print("Total words ending with 't' :",count)
    f.close()

# countEndT()

def CountEndTLines():
    f=open("DemoWrite.txt")
    count=0
    lines=f.readlines()
    for i in lines:
        if i.rstrip()[-1]=='t':
            count+=1
            print(i)
    print("Total lines ending with 't' :",count)
    f.close()