def SumEven():
    f=open("DemoWrite.text","r")
    sum=0
    data=f.read()
    for i in data:
        if i.isdigit():
            if int(i)%2==0:
                sum=sum+int(i)
    print("Sum of even digit is = ",sum)

SumEven()
