# f=open('DemoWrite.text','a') #append mode adds the data, dont overrwrites.
# f.write('\nfourth semester')  
# # list=['Computer\n', 'Mathematics\n','English']
# t=('Computer\n', 'Mathematics\n','English')
# f.writelines(t)  #It takes any type of string data

# f.close()

f=open("sumwrite.text",'a')
a=int(input("Enter first number"))
b=int(input("Enter second number"))
c=a+b
f.write('A = '+str(a))
f.write('\tB = '+str(b))
f.write('\tAddition = '+str(c))
f.close()