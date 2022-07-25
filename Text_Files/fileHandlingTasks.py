#program to count total no.of wors

# def countword():
#     f=open('Doc.txt','r')
#     text=f.read()
#     words = text.split()
#     count=0
#     for i in words:
#         count+=1

#     print("total no. of words",count)
# countword()

#program to count a specific word

# def CountWords():
#     f=open('Doc.txt','r')
#     text=f.read()
#     words = text.split()
#     count=0
#     for i in words:
#         if i=='Lorem':
#             count+=1

#     print("total no. of words",count)
# CountWords()


#program to count words having more than 5 occurence
def CountWords():
    f=open('Doc.txt','r')
    text=f.read()
    words = text.split()
    count=0
    for i in words:
        if len(i)>5:
            count+=1

    print("total no. of words >=5 are: ",count)
CountWords()
