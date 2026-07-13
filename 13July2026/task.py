import datetime

employees = [
    {"name": "Iftikhar", "dob": "20/5/97"},
    {"name": "Ali", "dob": "20/5/9"},
    {"name": "Ahmed", "dob": "25/5/95"},
    {"name": "Raza", "dob": "35/5/92"},
    {"name": "Saqlain"},
    { "dob": "20/9/93"},
]


# Assume date format is DD/MM/YYYY

# Print the list of employees with their Age.
# In case of date of birth not provided or not in correct format. Specify the proper msg
for employee in employees:
    name = None
    try:
        name = employee["name"]
        employee_age = datetime.date.strptime(employee["dob"], "%d/%m/%y")
        age = datetime.date.today() - employee_age
        print(f"Name: {name}, Age: {age.days // 365} years old")
    # except ValueError:
    #     print(f"Name: {name}, Age: - (date format issue)")
    # except KeyError:
    #     print(f"Name: {name}, Age: - (date not provided)")
    except Exception as e:
        print(f"Name: {name}, Age: -", e)