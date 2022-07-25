import pickle

def write():
    f=open("dict.dat","wb")
    d={}
    while True:
        r=int(input("Enter Rollno: "))
        n=input("Enter Name: ")
        m=int(input("Enter Marks: "))
        d['rollno']=r
        d['name']=n
        d['marks']=m

        pickle.dump(d,f)
        ch=input("Do you want to enter more records (Y/N)")
        if ch in "Nn":
            break
    f.close()





def read():
    f=open("dict.dat","rb")
    print("Reading records from dictionary...")
    try:
        while True:
            d=pickle.load(f)
            print(d)
    except EOFError:
        f.close()
write()
read()