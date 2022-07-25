from curses.ascii import islower, isupper


def TransferULO():
    f=open("DemoWrite.text","r")
    f1=open("UPPER.txt","w")
    f2=open("LOWER.txt","w")
    f3=open("OTHERS.txt","w")

    data=f.read()
    for i in data:
        if i.isupper():
            f1.write(i)
        elif i.islower():
            f2.write(i)
        else:
            f3.write(i)

    f.close()
    f1.close()
    f2.close()
    f3.close()
