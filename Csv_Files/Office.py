import csv

def write():
    f=open("employee.csv", "w", newline='')
    swriter=csv.writer(f)
    swriter.writerow(['EmpNo','EmpName','Salary'])
    rec=[]
    while True:
        eno=int(input("EmpNo: "))
        ename=input("EmpName: ")
        salary=int(input("Salary: "))
        data=[eno, ename, salary]
        rec.append(data)
        ch=input("More (Y/N)?")
        if ch in 'nN':
            break
    swriter.writerows(rec)
    print("Data written in Csv file successfully...")
    f.close()


def read():
    f=open("employee.csv","r")
    print("Reading data from a csv file..")
    sreader=csv.reader(f)
    next(sreader)
    for i in sreader:
        print(i)
    f.close()

def sumSalary():
    f=open("employee.csv","r")
    sreader=csv.reader(f)
    next(sreader)
    sum=0
    for i in sreader:
        sum=sum+int(i[2])
    print("Sum of salary of all employees: ",sum)
    f.close()

def countSalary():
    f=open("employee.csv","r")
    sreader=csv.reader(f)
    next(sreader)
    sum=0
    for i in sreader:
        if int(i[2])>30000:
            sum=sum+1
    print("Sum of salary greather than 30000: ",sum)
    f.close()

# write()
read()
sumSalary()
countSalary()