## TO print time and date

from datetime import datetime

# today = datetime.today()
# print("Today's date:", today)
	
d4 = today.strftime("%d-%m-%Y")
print("d4 =", d4)


# datetime object containing current date and time
now = datetime.now()
t1 = now.strftime("%H:%M:%S")
print("t1 = ", t1)

# dd/mm/YY H:M:S
# dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
# print("date and time =", dt_string)	
