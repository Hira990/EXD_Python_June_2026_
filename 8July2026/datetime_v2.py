import calendar, datetime

# User input for year
while True:
    input_year = int(input("Enter year: "))
    if input_year in range(1900, 2050):
        break
    else:
        print("Invalid Year. Please enter a valid year.")
print("Year is: ", input_year)

# User Input for month
list_of_months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
# either make a static dict like "janurary" : 1 or dynamic as below
dict_of_month = {}
for index, month in enumerate(list_of_months, start=1):
    dict_of_month[month] = index
while True:
    input_month = input("Enter month (format: March): ").lower()
    if input_month in list_of_months:
        break
    else:
        print("Invalid Month. Please enter a valid month.")
print("Month is: ", input_month)
input_month_sequence_number = dict_of_month[input_month]
print("Month Sequence Number: ", input_month_sequence_number)
max_days_in_month = calendar.monthrange(input_year, input_month_sequence_number)[1]
print("Max days allowed: ", max_days_in_month)

# User Input for day
while True:
    input_day = int(input(f"Enter day (range: 1-{max_days_in_month}): "))
    if input_day in range(1, max_days_in_month+1):
        break
    else:
        print("Invalid day. Please enter a valid day.")

user_date = datetime.date(input_year, input_month_sequence_number, input_day)
print("User Date Object Created: ", user_date)

# Ek month bad ki date print krni jo user ne di
date_after_one_month = user_date + datetime.timedelta(days=30)
print("Date After One Month: ", date_after_one_month)
print("Date After One Month: ", date_after_one_month.strftime("%d %B, %Y"))

