# cart = [
#     {"name": "laptop", "price": "34 USD", "qty": 1},
#     {"name": "c-type charger", "price": 5, "qty": 2},
#     {"name": "bluetooth", "price": 90, "qty": 3}
# ]
#
# # Calculate Final Bill, Show Total Bill
# # If Total Bill is greater than 200, Apply 15% discount
# # Show the Final Bill, if the discount applied
#
# total_bill_price = 0
# for cart_item in cart:
#     price = int(cart_item["price"]) * int(cart_item["qty"])
#     total_bill_price = total_bill_price + price
#
# print(f"Total bill price: {total_bill_price}")
#
# discount_applied = False
# if total_bill_price > 200:
#     discount = int(total_bill_price * 0.15)
#     print(f"Discount: {discount}")
#     discount_applied = True
#
# if discount_applied:
#     print(f"Discount Applied: {discount}")
#     final_bill = total_bill_price - discount
#     print(f"Final Bill: {final_bill}")
#

# =============================================

# cart = [
#     {"name": "laptop", "price": "34 USD", "qty": 1},
#     {"name": "c-type charger", "price": "5 USD", "qty": 2},
#     {"name": "bluetooth", "price": "90 USD", "qty": 3}
# ]
#
# print(cart[0]['price'])

# 34

# =============================================

# total_credit_hours = 72
# students = [
#     {"name": "Ali", "present_hours": 45},
#     {"name": "Ahmed", "present_hours": 67},
#     {"name": "Fahad", "present_hours": 56},
# ]
#
# # Get a list of dropped students
# # Dropped Students : (Attandence less than 75%)
# # Find Student with highest attendance in percentage
# # Find Student with lowest attendance in percentage.
#
# # Calculate attendance percentage
# for student in students:
#     percentage = round(student["present_hours"] * 100 / total_credit_hours, 2)
#     student["attendance_percentage"] = percentage
# print(students)
#
# # Get the student with highest percentage attendance
# student_with_highest_attendance = students[0]
# for student in students:
#     if student["attendance_percentage"] > student_with_highest_attendance["attendance_percentage"]:
#         student_with_highest_attendance = student
# print(student_with_highest_attendance["name"])
#
# # Get the student with lowest percentage attendance
# student_with_lowest_attendance = students[0]
# for student in students:
#     if student["attendance_percentage"] < student_with_lowest_attendance["attendance_percentage"]:
#         student_with_lowest_attendance = student
# print(student_with_lowest_attendance["name"])
#
# # Create a list of students, dropped due to attendance
# dropped_students = []
# for student in students:
#     if student["attendance_percentage"] < 75:
#         dropped_students.append(student)
#
# print(f"Dropped Students:")
# for student in dropped_students:
#     print(student["name"])


# ============================================================

employees = [
    {"name": "Ali", "base_salary": 30000, "overtime_hours": 6},
    {"name": "Ahmed", "base_salary": 40000, "overtime_hours": 2},
    {"name": "Ahsan", "base_salary": 40000, "overtime_hours": 0},
]
overtime_per_hour_rate = 500

# Calculate the final salary of all the employees, adding overtime

for employee in employees:
    if employee["overtime_hours"] > 0:
        employee["total_salary"] = employee["base_salary"] + (employee["overtime_hours"] * overtime_per_hour_rate)
        employee["overtime_applied"] = True
    else:
        employee["total_salary"] = employee["base_salary"]
        employee["overtime_applied"] = False

print(employees)
