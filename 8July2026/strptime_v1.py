import datetime

user_input_date = "2026-5-5"
user_input_date = "7/July/2026"
user_input_date = datetime.date.strptime(user_input_date, "%d/%B/%Y")
print(user_input_date)
print(type(user_input_date))

expiry_date = user_input_date + datetime.timedelta(days=30)

print(expiry_date)

