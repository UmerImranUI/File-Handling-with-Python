import pickle
from traceback import print_tb

def write():
    f=open("BinaryWrite.dat","wb")
    list=['Comp Sci','Maths','English','Physics']
    dic={'comp':100, 'Maths':98, 'English':79}
    
    pickle.dump(list, f)
    pickle.dump(dic, f)
    f.close()
def read():
    f=open("BinaryWrite.dat","rb")
    lst=pickle.load(f)
    d=pickle.load(f)
    print(lst)
    print(d)
    f.close()
write()
read()

    
write()
print('Data is written')