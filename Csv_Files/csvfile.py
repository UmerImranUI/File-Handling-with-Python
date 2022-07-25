import csv


f=open("Student.csv","w",newline="")
s_writer=csv.writer(f)
s_writer.writerow(['Roll No','Name','Marks'])
rec=[]
while True:
    r=int(input("Enter roll no: "))
    n=input("Enter Name: ")
    m=int(input("Enter marks: "))
    lst=[r, n, m]
    rec.append(lst)
    ch=input("Do you want to enter more records? (y/n)")
    if ch=='n':
        break
for i in rec:
    s_writer.writerow(i)

f.close()

def read():
    f=open("Student.csv", "r",newline="")
    s_reader=csv.reader(f)
    for i in s_reader:
        print(i)