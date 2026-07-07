employees = [
    {"name": "Ali", "base_salary": 30000, "overtime_hours": 6},
    {"name": "Ahmed", "base_salary": 40000, "overtime_hours": 2},
    {"name": "Ahsan", "base_salary": 40000, "overtime_hours": 0},
]
# overtime_per_hour_rate = 500
overtime_per_hour_rate = int(input("Enter the per hour rate for overtime: "))
print(overtime_per_hour_rate)
print(type(overtime_per_hour_rate))

# Calculate the final salary of all the employees, adding overtime

for e in employees:
    if e["overtime_hours"] > 0:
        e["total_salary"] = e["base_salary"] + (e["overtime_hours"] * overtime_per_hour_rate)
        e["overtime_applied"] = True
    else:
        e["total_salary"] = e["base_salary"]
        e["overtime_applied"] = False

print(employees)


# print("test1")
# # name = input()
# # print(f"Name is {name}")
# # print(type(name))
# age = input()
# print(f"Age: {age}")
# print(type(age))
# print("test2")