def Display():
    f=open("DemoWrite.txt","r")
    f1=open("nota.txt","w")
    while True:
        line=f.readline()
        if line=='':
            break
        if line[0]!='a':
            f1.write(line)
    
    f.close()
    f1.close()

Display()
print("Data written in the file...")