"""
module: datetime
1) datetime
2) date
3) time
4) timedelta
"""

# import datetime
# print(datetime.datetime.now())

"""
datetime -> 2026-07-07 13:02:59.538611
The date contains year, month, day, hour, minute, second, and microsecond.
"""
from datetime import datetime, timedelta

current_date_time = datetime.now()
print(f"Current date time: {current_date_time}. Type: {type(current_date_time)}")

custom_date = datetime(2020, 5, 17, 13, 19, 45)
print(f"Custom date time: {custom_date}. Type: {type(custom_date)}")

# Access the year, month, day, hour, minute, and seconds
print(custom_date.year)
print(custom_date.month)
print(custom_date.day)
print(custom_date.hour)
print(custom_date.minute)
print(custom_date.second)
expiry_date = f"{custom_date.month}/{custom_date.year}"
print(f"Expiry: {expiry_date}")

formatted_date = current_date_time.strftime("%d %B, %Y  %H:%M:%S")
print(formatted_date)
formatted_date = current_date_time.strftime("%d %B, %Y  %X")
print(formatted_date)
formatted_date = current_date_time.strftime("%d %B, %Y  %I:%M %p")
print(formatted_date)
formatted_date = current_date_time.strftime("%d %b, %y")
print(formatted_date)

print(current_date_time.strftime("%d %B, %Y  %I:%M %p"))
date_after_30_days = current_date_time - timedelta(days=15, hours=4)
print(date_after_30_days.strftime("%d %B, %Y  %I:%M %p"))

