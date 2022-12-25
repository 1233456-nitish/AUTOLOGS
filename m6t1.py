##Making the tkinter window functional
from datetime import datetime
import atexit
import tkinter as tk
import threading
import time


root = tk.Tk()

root.geometry("600x600")
root.title("LOGGER")

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
            pass
        # print('string exist')
        else:
        # print('string does not exist')
            heading()



label1 = tk.Label(root, text="AUTO LOG", font=("Arial", 30, 'bold'))
# label.configure(font=("Helvetica", 18, 'bold'))
label1.pack(padx=20, pady=10)

label2 = tk.Label(root, text="Input:", font=("Arial", 18))
label2.pack(padx=10, pady=5)

textbox1 = tk.Text(root, height=6, font=("Consolas", 14))
textbox1.pack(padx=10, pady=10)


def enter():
    global addedtext1
    addedtext1 = textbox1.get(1.0, tk.END)

button1 = tk.Button(root, text="Enter", font=("Arial", 18), command=enter)
button1.pack(padx=10, pady=10)

label2 = tk.Label(root, text="Inputs:", font=("Arial", 18))
label2.pack(padx=10, pady=5)

textbox2 = tk.Text(root, height=4, font=("Consolas", 14))
textbox2.pack(padx=10, pady=10)
textbox2.config(state= "disabled")

button2 = tk.Button(root, text="Exit", font=("Arial", 18))
button2.pack(padx=10, pady=10)


def loop():
    while True:
        now = datetime.now()
        t1 = now.strftime("%H:%M:%S")
    # print("t1 = ", t1)
   
        # addedtext1 = textbox1.get(1.0, tk.END)
        time.sleep(3)
        print(addedtext1)
    # addedtext = input('pls enter text:- ')
    
    
        text = t1 + " - " + addedtext1

        if addedtext1 == "":
            print(addedtext1)
        elif addedtext1 != "":
            with open(filename, 'a') as f:
                f.write(text+"\n")
        else:
            pass

threading.Thread(target=loop).start()    

root.mainloop()
