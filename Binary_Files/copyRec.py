import pickle

# def write():
#     f=open("Sports.dat","wb")
#     reclst=[]
#     while True:
#         e=input("Event: ")
#         p=input("Participant: ")
#         data=[e,p]
#         reclst.append(data)
#         ch=input("More (Y/N)?")
#         if ch in 'Nn':
#             break
#     pickle.dump(reclst, f)
#     f.close()


def read():
    f=open("Sports.dat","rb")
    rec=pickle.load(f)
    try:
        rec=pickle.load(f)
        for i in rec:
            print(i)
    except EOFError:
        f.close() 

def copy():
    f=open("Sports.dat","rb")
    f1=open("Athletic.dat","wb")
    reclst=[]
    try:
        rec=pickle.dump(f)
        for i in rec:
            if i[0]=='Athletics':
                reclst.append(i)
        pickle.dump(reclst, f1)
    except EOFError:
        f.close()
        f1.close()
# write()
read()
copy()