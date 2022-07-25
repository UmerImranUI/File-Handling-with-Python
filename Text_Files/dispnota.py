def DisplayNotA():
    f=open("DemoWrite.txt","r")
    f1=open("PoemNotA.txt","w")
    while True:
        line=f.readline()
        if line=='':
            break
        if 'a' not in line:
            f1.write(line)
    f.close()
    f1.close()
DisplayNotA()

