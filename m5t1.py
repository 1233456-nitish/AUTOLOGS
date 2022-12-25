import tkinter as tk
# from tkinter import *
# import _tkinter

root = tk.Tk()

root.geometry("600x600")
root.title("LOGGER")
root.iconbitmap('C:\CODING_RELATED_FILES\PYTHON_CODES\AUTOLOG\\text.png')


label1 = tk.Label(root, text="AUTO LOG", font=("Arial", 30, 'bold'))
# label.configure(font=("Helvetica", 18, 'bold'))
label1.pack(padx=20, pady=10)

label2 = tk.Label(root, text="Input:", font=("Arial", 18))
label2.pack(padx=10, pady=5)

textbox1 = tk.Text(root, height=6, font=("Consolas", 14))
textbox1.pack(padx=10, pady=10)

# myentry = tk.Entry(root)
# myentry.pack()

button1 = tk.Button(root, text="Enter", font=("Arial", 18))
button1.pack(padx=10, pady=10)

label2 = tk.Label(root, text="Last Input:", font=("Arial", 18))
label2.pack(padx=10, pady=5)

textbox2 = tk.Text(root, height=4, font=("Consolas", 14))
textbox2.pack(padx=10, pady=10)
textbox2.config(state= "disabled")

button2 = tk.Button(root, text="Exit", font=("Arial", 18))
button2.pack(padx=10, pady=10)


root.mainloop()


# https://youtu.be/ibf5cx221hk?t=1051