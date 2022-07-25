# f=open('Random.txt','w') #it will create the file(w), r only read it 
# f=open('Random.txt','r+') #it will create the file(w), r only read it 
#r+ make pointer to the end
# f=open('Random1.txt','a+')
f=open('Random1.txt','w+')
f.write('Umer is king') #if you open in w+, prev data will be overwritten
# print(f.read()) it will  not read bcz pointer in the end
f.seek(0) #now pointer goes to start
print(f.read())
f.close()