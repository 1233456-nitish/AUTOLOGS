## TO create a text file, rename it, and edit it.....
filename = "yo yo test1"
addedtext = input('pls enter text:- ')


with open(filename, "a") as f:
    f.write(addedtext+"\n")