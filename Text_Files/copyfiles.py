def Copy(s,d):
    f1=open(s,"r")
    f2=open(d,"w")
    data=f1.read()
    f2.write(data)
    f1.close()
    f2.close()

source=input("Enter source file(with. txt extension)")
destination=input("Enter destination file(with. txt extension)")
Copy(source, destination)