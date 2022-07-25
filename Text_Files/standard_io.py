import sys

sys.stdout.write("Enter file name: ")
file=sys.stdin.readline()
f=open(file.strip(),"r")

while True:
    ch=f.read(1)
    if ch=='':
        sys.stderr.write("End of File reached...")
        break
    else:
        print(ch, end='')
f.close()

# sys.stdout.write('Enter first number: ')
# a=int(sys.stdin.readline())

# sys.stdout.write('Enter second number: ')
# b=int(sys.stdin.readline())

# if b==0 :
#     sys.stderr.write("Can't divide any number by zero...")
# else:
#     sys.stdout.write("Division Possible...")