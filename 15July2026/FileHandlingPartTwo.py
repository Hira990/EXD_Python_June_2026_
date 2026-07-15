import json
from turtledemo.clock import display_date_time

# try:
#     with open("names.json") as file:
#         try:
#             list_of_students = json.load(file)
#             print(list_of_students)
#             print(type(list_of_students))
#             for student in list_of_students:
#                 print(student["name"])
#         except json.decoder.JSONDecodeError:
#             print("The file was not properly formatted")
#         except Exception as e:
#             print(f"Exception")
# except FileNotFoundError:
#     print("The file was not found...")
# except Exception as e:
#     print(f"Exception")


# """
# To add a list item in json names list
# """
# user_input = input("Enter a name: ")
# print(user_input)
#
#
# with open('only_names.json') as file:
#     names = json.load(file)
#
# print(names)
# print(type(names))
# names.append(user_input)
#
# print(names)
#
# with open('only_names.json', 'w') as file:
#     json.dump(names, file)
#     print("done")

"""
To remove a name
"""
user_input = input("Enter a name: ")
print(user_input)

with open('only_names.json') as file:
    names = json.load(file)
names = [name.lower() for name in names]

try:
    names.remove(user_input.lower())
    with open('only_names.json', 'w') as file:
        json.dump(names, file)
        print("done")
except ValueError:
    print("Sorry, thae name is not in the list")

