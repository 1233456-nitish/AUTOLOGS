#TO create a file, add date to the top, take input , print date with input.i
from datetime import datetime
import atexit

today = datetime.today()
d1 = today.strftime("%d-%m-%Y")
print("d1 =", d1)


filename = d1+".txt"


def breaker():
    with open(filename, 'a') as f:
        f.write("\n"+'--BREAK--' +"\n"+"\n")
atexit.register(breaker)


def heading():
    with open(filename, 'a') as f:
        f.write(d1+"\n"+"\n")


global date 
date = True


def Date():
    print(d1)
    # date = 1
    print(date)


with open(filename, 'a') as f:
    with open(filename, 'r') as f:
        content = f.read()
        if d1 in content:
            print("")
        # print('string exist')
        else:
        # print('string does not exist')
            heading()

while True:
    now = datetime.now()
    t1 = now.strftime("%H:%M:%S")
    print("t1 = ", t1)
   
    addedtext = input('pls enter text:- ')
    
    text = t1 + " - " + addedtext
    
    if addedtext == "":
        print(addedtext)
    else:
        with open(filename, 'a') as f:
            f.write(text+"\n")

