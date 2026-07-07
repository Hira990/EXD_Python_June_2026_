"""
User se input lein ek date...
Check krain k ye date future ki ha ya past ki

"""
from datetime import datetime, timedelta

year = int(input("Enter year"))
month = int(input("Enter month"))
day = int(input("Enter day"))

user_input_date = datetime(year, month, day, 16, 55, 24)
print(user_input_date)
print(datetime.dtoday())

if datetime.today() > user_input_date:
    print("date past")
elif datetime.today() < user_input_date:
    print("date future")
else:
    print("date today")


"""
User year enter kryga 4 digit me. chcek krna ha k sai year ha ya nai
month ap us se full month name lein gy. or 12 months me se nahe ha to sai lena ha
or day 1 se 31 user se input leni ha
"""