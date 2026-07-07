"""

function define krna ha ap ne "def" k keyword se
function name likhny k rules, similar to variable names


Simple Functions...

def print_hello_message():
    print("Hello World V1")
    print("Hello World V2")

print("hello testing")
print("Hello World V1")
print("Hello World V2")
# print_hello_message()


Functions with parameters

def calculate_sum(a, b):
    sum = a + b
    print(sum)

calculate_sum(1, 2)
"""

# def calculate_sum(num1, num2, num3=0):
#     sum = num1 + num2 + num3
#     print(sum)
#
# calculate_sum(1, 2, 3)

# def get_greeting():
#   print("Hello from a function")
#   return 65789
#
# message = get_greeting()
# print(message)
#
# def my_function(fname, lname):
#   print(fname + " " + lname)
#   print(f"{fname} {lname}")
#
# my_function("Emil", "aschak")
#
# def add_customer_in_db(name, phone, email, city, interest, previous_orders):
#     print(name, phone, email, city, interest, previous_orders)
#     print("customer added into db")
#
#
# previous_orders = input("Enter your previous orders: ")
# email = input("Enter your email: ")
# name = input("Enter your name: ")
# city = input("Enter your city: ")
# phone = input("Enter your phone number: ")
# interest = input("Enter your interest: ")
#
# add_customer_in_db(previous_orders=previous_orders,
#                    name=name, phone=phone, email=email,
#                    city=city, interest=interest)

def my_function(name, age, /):
  print("Hello", name)

my_function("Emil", age=23)