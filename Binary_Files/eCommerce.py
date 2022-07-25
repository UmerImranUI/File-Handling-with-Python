import pickle
def writerecords(n):
    f=open("Item.dat","wb")
    for i in range(0, n):
        Item_No=int(input("Enter Item No. :"))
        Item_Name=input("Enter Item Name :")
        Qty=int(input("Enter Quantity: "))
        Price=int(input("Enter Price: "))
        rec=[Item_No, Item_Name, Qty, Price]
        pickle.dump(rec, f)
    f.close()

def readrecords(n):
    f=open("Item.dat","rb")
    for i in range(0, n):
        data=pickle.load(f)
        print("Item No. :",data[0])
        print("Item Name :",data[1])
        print("Quantity :",data[2])
        print("Price per Item :", data[3])
        print("Amount :", data[2]*data[3])
    f.close()

n=int(input("number of records to be enter? "))
# writerecords(n)
readrecords(n)