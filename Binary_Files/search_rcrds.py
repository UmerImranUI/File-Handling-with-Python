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
            break
    pickle.dump(record, f)

def read():
    f=open("BinaryRecord.dat", 'rb')
    s=pickle.load(f)
    for i in s:
        rno=i[0]
        name=i[1]
        marks=i[2]
        print(rno, name, marks)



def Append():
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
    pickle.dump(record, f)
    f.close()

def read():
    f=open("SampleData.dat",'rb')
    while True:
        try:
            s=pickle.load(f)
            for i in s:
                print(i)
        except EOFError:
            break
    f.close()


def search():
    f=open("BinaryRecord.dat",'rb')
    s=pickle.load(f)
    rno=int(input("Enter the rollno. you want to search"))
    found=0
    for i in s:
        if i[0]==rno:
            print(i)
            found=1
            break
    
    if found==0:
        print("not found")
write()
# read()
# Append()
# read()
search()