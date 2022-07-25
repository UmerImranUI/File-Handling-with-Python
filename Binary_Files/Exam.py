import pickle

def write():
    f=open("EXAM.DAT","wb")
    while True:

        Exam_id=int(input("Enter Exam - ID: "))
        Exam_Name=input("Enter Exam Name: ")
        Date_of_Exam=input("Enter Date of Exam: ")
        Total_candidates=int(input("Enter Total candidates: "))
        data=[Exam_id, Exam_Name, Date_of_Exam, Total_candidates]
        pickle.dump(data, f)
        ch=input("Do you want to enter more (y/n) ?")
        if ch in 'nN':
            break
    f.close()


def read():
    f=open("EXAM.DAT", "rb")
    try:
        while True:
            data=pickle.load(f)
            print(data)
    except EOFError:
        f.close()

def countexam():
    f=open("EXAM.DAT","rb")
    count=0
    sum=0
    print("-------------------------")
    try:
        while True:
            data=pickle.load(f)
            sum=sum+int(data[3])
            if int(data[3])>25000:
                count+=1
                print(data)
    except EOFError:
        f.close()
    print("Total number of candidates for all exams: ", sum)




# write()
read()
countexam()