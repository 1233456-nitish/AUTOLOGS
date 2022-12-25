#TO check if date is already printed
from datetime import datetime

# string to search in file
today = datetime.today()
d1 = today.strftime("%d-%m-%Y")
print("d1 =", d1)

filename = d1+".txt"

with open(filename, 'r') as fp:
    content = fp.read()
    if d1 in content:
        print('string exist')
    else:
        print('string does not exist')