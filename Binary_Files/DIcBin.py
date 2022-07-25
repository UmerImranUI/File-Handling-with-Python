
import pickle

from numpy import searchsorted

def write():
    player={}
    f=open("Players.dat","wb")
    while True:
        pcode=input("Player Code: ")
        pname=input("Player Name: ")
        runs=input("Total Runs: ")
        pcountry=input("Player Country: ")
        player['Code']=pcode
        player['Name']=pname
        player['Total Runs']=runs
        player['Country']=pcountry
        pickle.dump(player, f)
        ch=input("More(y/n)?")
        if ch in 'Nn':
            break
    f.close()

def read():
    f=open("Players.dat","rb")
    player={}
    try:
        while True:
            player=pickle.load(f)
            print(player)
    except EOFError:
        f.close()

def searchCountry():
    f=open("Players.dat","rb")
    player={}
    count=found=0
    c=input("Enter country: ")
    try:
        while True:
            player=pickle.load(f)
            if player['Country']==c:
                count+=1
                found=1
    except EOFError:
        f.close()
    if found==0:
        print("Sorry...not found")
    else:
        print("Total no. of players",c,"are: ",count)


def searchA():
    print("Displaying the players whose name startwith A :")
    f=open("Players.dat","rb")
    player={}
    count=found=0
    try:
        while True:
            player=pickle.load(f)
            if player['Name'].startswith('A')==True:
                print(player)
                found=1
    except EOFError:
        f.close()
    if found==0:
        print("Sorry...not found")

def SearchRuns():
    print("Displaying the players whose name startwith A :")
    f=open("Players.dat","rb")
    player={}
    count=found=0
    try:
        while True:
            player=pickle.load(f)
            if player['Total Runs']>str(80):
                print(player)
                found=1
    except EOFError:
        f.close()
    if found==0:
        print("Sorry...not found")
# write()
# read()
# searchCountry()
# searchA()
SearchRuns()