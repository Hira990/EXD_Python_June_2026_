import datetime

date = "9-07-2026"
time = "09:30"

date_time = f"{date} {time}"
print(date_time)

date_time_object = datetime.datetime.strptime(date_time, "%d-%m-%Y %H:%M")
print(date_time_object)
print(date_time_object)

print(date_time_object)

