import random

def ReadRandomLine():
    f=open("DemoWrite.text","r")
    lines=f.readlines()
    length=len(lines)
    r1=random.randint(0, length-1)
    print(lines[r1])
    f.close()
ReadRandomLine()