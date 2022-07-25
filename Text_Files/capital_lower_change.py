def CapitalReplace():
    f=open("DemoWrite.text", "r+")
    data=f.read()
    f.seek(0)
    for i in data:
        if i.isupper():
            f.write(i.islower())
        else:
            f.write(i)
    f.close()