import random
import os
import getch
from colorama import *


#start of pos() function
#pos() returns string of ANSI CODE
def pos(x,y):
    return '\x1b['+str(y)+';'+str(x)+'H'
#end of pos() function

#board function prints the 4X4 board
def board(l):
    """
    takes list as an arguement
    """
    print("{loc}{styl}|------|------|------|------|".format(loc=pos(30,5),styl=Style.BRIGHT))
    i=0
    x=4
    while i<x:
        print("{loc}{styl}{z}{y}|{a}{b}{c:6s}{z}{y}|{d}{e}{f:6s}{z}{y}|{g}{h}{n:6s}{z}{y}|{j}{k}{m:6s}{z}{y}|".format(styl=Style.BRIGHT,loc=pos(30,5+(i*2)+1),z=Fore.RESET,y=Back.RESET,a=num_fore_col[str(l[i*x+0])],b=num_back_col[str(l[i*x+0])],c=str(l[i*x+0]),d=num_fore_col[str(l[i*x+1])],e=num_back_col[str(l[i*x+1])],f=str(l[i*x+1]),g=num_fore_col[str(l[i*x+2])],h=num_back_col[str(l[i*x+2])],n=str(l[i*x+2]),j=num_fore_col[str(l[i*x+3])],k=num_back_col[str(l[i*x+3])],m=str(l[i*x+3])))
        print("{loc}{styl}|------|------|------|------|".format(styl=Style.BRIGHT,loc=pos(30,5+(i*2)+2)))
        i+=1
    print("\n")
#end of board() function


#start of shift() function
#shift function shifts the elements to left and add them properly
def shift(l):
    """
    takes list as an arguement
    """
    def leftmover(l):
        """
        takes list as an arguement
        """
        m=list(filter(lambda i : i!=' ',l))
        x=len(m)
        while x<4:
            m.append(' ')
            x+=1
        return m

    def adder(l):
        """
        takes list as an arguement
        """
        for count,item in enumerate(l[:3]):
            if item==' ':
                break
            else:
                if l[count]==l[count+1] and l[count]!=' ':
                    l[count]+=l[count+1]
                    global score
                    score +=l[count]
                    l[count+1]=' '
                    l=leftmover(l)
        return l



    l=leftmover(l)
    l=adder(l)
    return l
#end of shift() function

#start of isstopped() function
#isstopped checks whether there are any possibilities or not
def isstopped(l):
    i=0
    j=0
    while i<16:
        j=0
        while j<3:
            if (l[i+j]==l[i+j+1]):
                return False
            j+=1
        i+=4
    i=0
    j=0
    while i<4:
        j=0
        while j<3:
            if l[i + j*4] == l[i +(j+1)*4]:
                return False
            j+=1
        i+=1
    return True
#end of isstopped() function

#start of check() function
#check funtion returns the a list of indices of empty spaces
def check(l):
    """
    takes list as an arguement
    """
    emptylist=[]
    for i, item in enumerate(l):
        if item==' ':
            emptylist.append(i)
    return emptylist
#end of check function

#start of fillemptylist() funtion
#fillemptylist() function fills any of the empty space with [2 or 4]
def fillemptylist(l,emptylist):
    l[random.choice(emptylist)]=random.choice(filler)
    return l
#end of fillemptylist() function

#start of move function
#move function moves the list in x direction
def move(x,l):
    """
    takes 2 arguements - a character and a list
    """
    nestlist=[]
    counter=0
    temp=list(l)

    if x=='w'or x=='W':
        while counter<4:
            nestlist.append(l[counter:16:4])
            counter+=1
        shifted=list(map(shift,nestlist))
        for i ,j in enumerate(shifted):
            for k , item in enumerate(j):
                l[i+k*4]=item

    elif x=='s' or x=='S':
        while counter<4:
            nestlist.append(l[12+counter::-4])
            counter+=1
        shifted=list(map(shift,nestlist))
        for i ,j in enumerate(shifted):
            for k , item in enumerate(j):
                l[i+(3-k)*4]=item

    elif x=='a' or x=='A':
        while counter<4:
            nestlist.append(l[counter*4:(counter*4)+4:1])
            counter+=1
        shifted=list(map(shift,nestlist))
        for i ,j in enumerate(shifted):
            for k , item in enumerate(j):
                l[i*4+k]=item

    elif x=='d' or  x=='D':
        while counter<4:
            r=l[counter*4:(counter*4)+4:1]
            nestlist.append(r[::-1])
            counter+=1
        shifted=list(map(shift,nestlist))
        for i ,j in enumerate(shifted):
            for k , item in enumerate(j):
                l[i*4+3-k]=item
    else:
        pass


    if (x=='w' or x=='W' or x=='s' or x=='S' or x=='a' or x=='A' or x=='d' or x=='D') and temp!=l:
        emptylist=check(l)
        l=fillemptylist(l,emptylist)

    return l
#end of move() function

#start of gamestart() function
#game start function starts the game
def gamestart():
    """
    takes no arguements
    """
    global fore_col,back_col,num_fore_col,num_back_col,score,filler
    fore_col=(Fore.BLACK,Fore.BLUE,Fore.CYAN,Fore.MAGENTA,Fore.RED,Fore.GREEN,Fore.YELLOW,Fore.WHITE,Fore.RESET)
    back_col=(Back.BLACK,Back.BLUE,Back.CYAN,Back.MAGENTA,Back.RED,Back.GREEN,Back.YELLOW,Back.WHITE,Back.RESET)
    num_back_col={' ':Back.RESET,'2':Back.BLACK,'4':Back.BLUE,'8':Back.CYAN,'16':Back.MAGENTA,'32':Back.RED,'64':Back.GREEN,'128':Back.YELLOW,'256':Back.BLACK,'512':Back.BLUE,'1024':Back.CYAN,'2048':Back.WHITE,'4096':Back.MAGENTA,'8192':Back.RED,'16384':Back.GREEN,'32768':Back.YELLOW,'65536':Back.WHITE,'131072':Back.BLUE}
    num_fore_col={' ':Fore.RESET,'2':Fore.WHITE,'4':Fore.WHITE,'8':Fore.WHITE,'16':Fore.WHITE,'32':Fore.WHITE,'64':Fore.WHITE,'128':Fore.WHITE,'256':Fore.WHITE,'512':Fore.WHITE,'1024':Fore.WHITE,'2048':Fore.BLACK,'4096':Fore.MAGENTA,'8192':Fore.WHITE,'16384':Fore.WHITE,'32768':Fore.WHITE,'65536':Fore.BLACK,'131072':Fore.BLACK}
    score =0
    filler =[2,2,2,2,2,2,2,2,4,2]

    init(autoreset=True) #initializes colors
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\t \t ***2048****")
    print("==============")
    print("W - to move up")
    print("S - to move down")
    print("A - to move left")
    print("D - to move right")
    print("==============")
    while True:
            print('press Y to Start the game and N to exit:  ',end="")
            x = getch.getche()
            print("")
            if x== 'Y' or x=='N' or x=='y' or x=='n':
                break
            else:
                print("wrong input try again")

    if x=='Y' or x=='y':
        l=[' ']*16
        emptylist=check(l)
        l=fillemptylist(l,emptylist)
        emptylist=check(l)
        l=fillemptylist(l,emptylist)
        os.system('cls' if os.name == 'nt' else 'clear')
        while True:
            print("{loc}{styl}****2048****".format(loc=pos(38,2),styl=Style.BRIGHT))
            print("{loc}{styl}============".format(loc=pos(38,3),styl=Style.BRIGHT))
            print("{styl}score : {scor}".format(scor=score,styl=Style.BRIGHT))
            print("\n")
            board(l)
            print('make your move: ',end="")
            l=move(getch.getche(),l)
            print("")
            os.system('cls' if os.name == 'nt' else 'clear')
            emptylist=check(l)
            if len(emptylist)==0:
                print("{loc}{styl}****2048****".format(loc=pos(38,2),styl=Style.BRIGHT))
                print("{loc}{styl}============".format(loc=pos(38,3),styl=Style.BRIGHT))
                print("{styl}score : {scor}".format(scor=score,styl=Style.BRIGHT))
                if(isstopped(l)):
                    board(l)
                    print('gameover')
                    break

#end of gamestart() function


gamestart()
