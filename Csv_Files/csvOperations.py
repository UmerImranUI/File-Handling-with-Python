import csv

def write():
    f=open("Items.csv","w", newline="")
    swriter=csv.writer(f)
    swriter.writerow(['InNO','IName','Qty','Price'])
    rec=[]
    while True:
        n=int(input("Item No: "))
        name=input("Item Name: ")
        qty=int(input("Quantity: "))
        price=int(input("Price: "))
        data=[n,name,qty,price]
        rec.append(data)
        ch=input("More (Y/N)?")
        if ch in 'nN':
            break

    swriter.writerows(rec)
    print("Data written in CSV Filesuccessfully...")
    f.close()

def read():
    f=open("Items.csv","r")
    print("Reading the data...")
    sreader=csv.reader(f)
    for i in sreader:
        print(i)

    f.close()

def search():
    f=open("Items.csv","r")
    print("Searching data from a csv file...")
    s=input("Enter Item No. to be searched: ")
    found=0
    sreader=csv.reader(f)
    for i in sreader:
        if i[0]==s:
            print(i)
            found=1
    
    if found==0:
        print("Sorry.. No record found...")
    f.close()


def searchPrice():
    f=open("Items.csv","r")
    print("Displaying records b/w 10000 and 60000")
    sreader=csv.reader(f)
    found=0
    next(sreader)
    for i in sreader:
        if i[3]>str(10000):
            print(i)
            found=1
    if found==0:
        print("Sorry... No record found..")
    f.close()

# write()
# read()
search()
# searchPrice()