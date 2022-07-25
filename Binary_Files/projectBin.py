import pickle

def write():
    f=open("BinaryRecord.dat",'wb')
    record=[]
    while True:
        rno=int(input('Enter roll no: '))
        name=input('Enter name: ')
        marks=int(input('Enter marks: '))
        data=[rno,name,marks]
        record.append(data)
        ch=input("Do you want to enter more data? (y/n)")
        if ch=='n':
            
            pickle.dump(record, f)
            print("Record Added..")
            f.close()
            break

def read():
    print("Contents in a File")
    f=open("BinaryRecord.dat",'rb')
    while True:
        try:
            s=pickle.load(f)
            for i in s:
                print(i)
        except Exception:
            f.close()
def append():
    print("to append data..")
    f=open("BinaryRecord.dat",'ab')
    record=[]
    while True:
            rno=int(input('Enter roll no: '))
            name=input('Enter name: ')
            marks=int(input('Enter marks: '))
            data=[rno,name,marks]
            record.append(data)
            ch=input("Do you want to enter more data? (y/n)")
            if ch=='n':
                break
    f.seek(0)
    pickle.dump(record, f)
    print("Record Appended...")
    f.close()

def search():
    f=open("BinaryRecord.dat",'rb')
    s=pickle.load(f)
    rno=int(input("Enter the rollno. you want to search"))
    found=0
    try:
        for i in s:
            if i[0]==rno:
                print(i)
                found=1
                break
    except EOFError:
        f.close()
    if found==0:
        print("not found")

def update():
    f=open("BinaryRecord.dat",'r+')
    s=pickle.load(f)
    rno=int(input("Enter roll no whose record you want to update..."))
    f.seek(0)
    try:
        while True:
            rpos=f.tell()
            s=pickle.load(f)
            print(s)
            for i in s:
                if rno==i[0]:
                    print("Current name is: ",i[1])
                    i[1]=input("Enter updated name: ")                    
                    i[2]=input("Enter updated marks: ")                    
                    f.seek(rpos)
                    pickle.dump(s, f)
                    break
    except Exception:
        f.close()

def delete():
    f=open("BinaryRecord.dat","rb")
    s=pickle.load(f)
    f.close()
    r=int(input("Enter roll no to be deleted: "))
    f=open("BinaryRecord.dat","wb")
    print(s)
    reclst=[]
    for i in s:
        if i[0]==r:
            continue
        reclst.append(i)
    pickle.dump(reclst, f)
    f.close()
            
def MainMenu():
    print("----------------------------------------")
    print("1. Write Data in a Binary File...")
    print("2. Read Data from a File...")
    print("3. Append Fata in a File...")
    print("4. Search Operation in a File...")
    print("5. Update Data in a File...")
    print("6. Delete Operation in a File...")
    print("7. Exit...")
    print("-----------------------------------------")

while True:
    MainMenu()
    ch=int(input("Enter your choice: "))
    if ch==1:
        write()
    elif ch==2:
        read()
    elif ch==3:
        append()
    elif ch==4:
        search()

    elif ch==5:
        update()

    elif ch==6:
        delete()
    elif ch==7:
        break
