# def read():
#     f=open('doc.txt')
#     while True:
#         s=f.readline()
#         if s=='':
#             break
#         else:
#             print(s)

# read()

# def read():
#     f=open('doc.txt')
#     lines=f.readlines()
#     count=0
#     for i in lines:
#         if i[0]=='F' or i[0]=='D':
#             count=count+1
#             print(i)
#     print("Total no. of lines starts with F are",count)

# read()


def BIGLINES():
    f=open("Doc.txt", "r")
    lines=f.readlines()
    for i in lines:
        if len(i)>=50:
            print(i)

BIGLINES()