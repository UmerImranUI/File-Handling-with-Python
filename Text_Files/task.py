def read():
    f=open("DemoWrite.text", "r")
    data=f.read()
    count=0
    words=data.split()
    for i in words:
        if i[-1]=='e':
            print(i, end='\n')

read()

def ev_dig_read():
    f=open("DemoWrite.text","r")
    sum=0
    data=f.read()
    for i in data:
        if i.isdigit():
            if int(i)%2==0:
                print(i)
                sum=sum+int(i)
    print("Sum of even digits: ",sum)
ev_dig_read()