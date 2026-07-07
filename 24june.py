def call_web_scrapper():
    # return None
    return "iftikhar@gmail.com"


# # print("this is my marks")
# # print(554)
# # print(34534.34534)

# # a = "7" # coming from another system
# # marks = 56
# # total = a + str(marks)
# # print(total)
# # total = int(a) + marks
# # print(total)

# # a = 6
# # if a > 9:
# #     print(this is ok)


# # print("yes")

# total_number_of_rooms = 7
# totalnumberofrooms = 7
# totalNumberOfRooms = 7
# total_rooms = 7  # total number of rooms

# # this is comment
# firstname = "iftikhar"  # sdfv
# first_name = "iftikhar"


# print("data is passed to the server, student: " + first_name)
# print("data is passed to the server, student:", first_name)
# print(f"data is passed to the server, student: {first_name}")


# a = None
# if a:
#     print("a has some value")
# else:
#     print("a does not have")

# email_add_received = call_web_scrapper()
# if email_add_received:
#     print(f"Email Address is {email_add_received}")
# else:
#     print("Email Address not received")

# a = """Lorem ipsum dolor sit amet, consectetur adipiscing elit,
# sed do eiusmod tempor incididunt ut labore et
# dolore magna aliqua."""
# print(a)


patients = ["iftikhar", "ahmed", "noman", "raza", "ali"]
# print(patients)
# print(type(patients))
# print(patients[-1])
# print(patients[0:3])

# patients = ["iftikhar", "ahmed", "noman", "raza", "saqlain", "iftikhar"]
# # patients.remove("iftikhar")
# patients.append("sa2")
# print(patients)
# # new_patient = "usman"

# # if new_patient in patients:
# #     print(f"{new_patient} is present in the list")
# # else:
# #     print(f"{new_patient} is not present in the list")


# patients = ["iftikhar", "ahmed", "noman", "raza", "saqlain", "iftikhar2"]
# new_patient = "raza"

# for patient in patients:
#     if patient == new_patient:
#         print("patient matched")
#     else:
#         print("not matched")
#     # custom_name = i + " 1234567890"
#     # print(custom_name)

# if new_patient in patients:
#     print(f"{new_patient} already exists in system")


# for i in range(10):
#     print(i)  # api call

# Generate a random number between 1 to 50, store it in a variable
# Make a list of 50 integers with those random numbers

# generate again a single random number
# check if it exists in the list or not

# import random
# list_of_numbers = []

# for i in range(20):
#     random_number = random.randint(1,100)
#     list_of_numbers.append(random_number)

# print(list_of_numbers)

# number_to_match = 56
# if number_to_match in list_of_numbers:
#     print(f"We have found {number_to_match} in the list")

# student = {
#     "name": "iftikhar",
#     "age": 29,
#     "email": "test@gmail.com",
#     "phone_nums": [1234, 346534],
#     "primary_ph": 21412,
#     "secondary_ph": [234235,23423523]
# }

# print(student["age"])
# print(type(student["age"]))


# print(student["secondary_ph"])
# print(type(student["secondary_ph"]))
# print(student["secondary_ph"][0])
# print(type(student["secondary_ph"][0]))

students = ["iftikhar", "ahmed"]

students = [["iftikhar", 29], ["ahmed", 28]]

students = [
    {
        "name": "iftikhar",
        "age": 29
    },
    {
        "name": "ahmed",
        "age": 28

    },
    {
        "name": "ali",
        "age": 26

    }
]
final_students = []

for student in students:
    # print(student["name"])
    print(f"{student["name"]}, Age: {student["age"]}")
    if student["age"] > 25:
        print("this one")
        final_students.append(student)

print(final_students)