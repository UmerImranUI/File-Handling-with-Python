import pickle

def write():
    f=open("StudentDetails.dat","wb")
    while True:
        r=int(input("Enter Roll No: "))
        n=input("Enter Name: ")
        Data=[r,n]
        pickle.dump(Data, f)
        ch=input("More? (Y/N)")
        if ch in 'Nn':
            break
    f.close()


def read():
    f=open("StudentDetails.dat","rb")
    try:
        while True:
            rec = pickle.load(f)
            print(rec)
    except EOFError:
        f.close()


def search():
    found=0
    rollno=int(input("Enter roll no whose name you want to search: "))
    f=open("StudentDetails.dat","rb")
    try:
        while True:
            rec = pickle.load(f)
            if rec[0]==rollno:
                print(rec[1])
                found=1
    except EOFError:
        f.close()
    if found==0:
        print("Sorry... No record found...")

search()
# write()
read()