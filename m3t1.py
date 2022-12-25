#TO create a file, add date to the top, take input , print date with input.
from datetime import datetime

today = datetime.today()
d1 = today.strftime("%d-%m-%Y")
print("d1 =", d1)

filename = d1+".txt"

# file = open(filename, 'a')
# head = 0

# def heading():
#     with open(filename, 'a') as f:
#         f.write(d1+"\n"+"\n")
#     head = 1


 
while True:
    now = datetime.now()
    t1 = now.strftime("%H:%M:%S")
    print("t1 = ", t1)
   
    addedtext = input('pls enter text:- ')
    
    text = t1 + " - " + addedtext
    # t2 = text.replace(str(addedtext), ' ')
    # t2 = text.replace("-", '')
    # t2 = text.translate({ord(str(addedtext)): None})
    # print("t2 = ", t2)

    # if head == 1:
    #     continue
    # else:
    #     heading()

    # file.write(text+"\n")
    with open(filename, 'a') as f:
        # if t2 == t1:
        #     f.write(" " + addedtext)
        # elif t2 != t1:
        # heading()
        f.write(text+"\n")
        # else:
            # break


    if addedtext == '~':
        with open(filename, 'a') as f:
            f.write("\n"+'--BREAK--' +"\n"+"\n")
        quit()
    # elif addedtext == "":
    #     with open(filename, 'a') as f:
    #         f.write("")
    else:
        continue

        

        # file.insert("\n"+text)
        

# print(text)


