from curses.ascii import isupper


def write():
    f=open("WriteorEnd.txt","w")
    while True:
        data=input("Enter any string or 'END' to exit. ")
        if data.upper()=='END':
            break
        else:
            f.write(data+'\n')
    f.close()
# write()


def read():
    f=open("WriteorEnd.txt","r")
    lines=f.readlines()
    for i in lines:
        if i[0].isupper():
            print(i)

    f.close()

read()
