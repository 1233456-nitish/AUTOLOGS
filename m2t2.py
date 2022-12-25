## TO create a text file, rename it, and edit it.....
import os

# file = open('File1.txt', 'w+')

# str1 = 'Hello World. Keep Smiling!'


# Writing a string to the file using the write() method of file object
# file.write(str1)

# file.close()
with open(filename, 'a') as f:
    f.write(text+"\n")

## the a in colons is for appending new text at the end of the file ......

