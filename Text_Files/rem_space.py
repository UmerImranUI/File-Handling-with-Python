def RemoveSpace():
    f=open("Pythonspace.txt","r")
    f1=open("PythonRemovespace.txt","w")
    data=f.read()
    word=data.split()
    s=''.join(word)
    f1.write(s)
    print("Data written successfully")

RemoveSpace()
