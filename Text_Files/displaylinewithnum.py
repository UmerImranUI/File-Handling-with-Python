def LineNumber():
    f=open("DemoWrite.text","r")
    count=1
    while True:
        line=f.readline()
        if line=='':
            break
        else:
            print(count, ":",line,end='')
            count+=1
    f.close()
LineNumber()
