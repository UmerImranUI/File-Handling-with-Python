def ReadCorrespondingLines():
    f1=open("DemoWrite.txt","r")
    f2=open("copied.txt","r")
    f3=open("Merge.txt","w")
    lines1=f1.readlines()
    lines2=f2.readlines()
    for i in range(len(lines1)):
        merge=lines1[i]+lines2[i]
        f3.write(merge)
    f1.close()
    f2.close()
    f3.close()
    print("Data written to a file successfully...")

ReadCorrespondingLines()