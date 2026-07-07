# import random
#
# original_list = ["Alice", "Bob", "Charlie", "David", "Emma", "Frank", "Grace", "Henry", "Isabella", "Jack", "Katherine", "Liam", "Mia", "Noah", "Olivia", "Peter", "Quinn", "Ryan", "Sophia", "Thomas"]
# max_index = len(original_list) - 1
#
# # Change the list to dict (to store index in key)
# for index, value in enumerate(original_list):
#     patient_dict = {
#         "name": value,
#         "index": index
#     }
#     original_list[index] = patient_dict
#
# mid_index_value = int(len(original_list)/2)
# random_index_list = []
#
# while len(random_index_list) < mid_index_value:
#     random_number = random.randint(0, max_index)
#     if random_number not in random_index_list:
#         random_index_list.append(random_number)
#
# print(random_index_list)
#
# new_original_list = []
# for num in random_index_list:
#     new_original_list.append(original_list[num])
#
# print(new_original_list)
#
# print("Half Done")
#
# while len(random_index_list) < mid_index_value:
#     random_number = random.randint(0, max_index)
#     if random_number not in random_index_list:
#         random_index_list.append(random_number)
#
#
# random_patient = random.sample(random_index_list, 5)
# print(random_patient)
# for i in random_patient:
#     print(original_list[i]['name'])


# ======================================================================

students = [
    {"name": "Alice", "marks": [45, 56, 43, 57, 39]},
    {"name": "Bob", "marks": [67, 72, 58, 64, 70]},
    {"name": "Charlie", "marks": [81, 76, 89, 84, 78]},
    {"name": "David", "marks": [52, 48, 61, 55, 59]},
    {"name": "Emma", "marks": [91, 88, 94, 90, 93]}
]

# students = [
#     {"name": "Alice", "marks": [45, 56, 43, 57, 39], "max": 57, "min": 39, "avg": 23},
#     {"name": "Bob", "marks": [67, 72, 58, 64, 70], "max": 57, "min": 39, "avg": 23},
#     {"name": "Charlie", "marks": [81, 76, 89, 84, 78], "max": 57, "min": 39, "avg": 23},
#     {"name": "David", "marks": [52, 48, 61, 55, 59], "max": 57, "min": 39, "avg": 23},
#     {"name": "Emma", "marks": [91, 88, 94, 90, 93], "max": 57, "min": 39, "avg": 23}
# ]
# students = [
#     {'name': 'Alice', 'marks': [45, 56, 43, 57, 39], 'max_mark': 57, 'min_mark': 39, 'avg_mark': 48.0},
#     {'name': 'Bob', 'marks': [67, 72, 58, 64, 70], 'max_mark': 72, 'min_mark': 58, 'avg_mark': 66.2},
#     {'name': 'Charlie', 'marks': [81, 76, 89, 84, 78], 'max_mark': 89, 'min_mark': 76, 'avg_mark': 81.6},
#     {'name': 'David', 'marks': [52, 48, 61, 55, 59], 'max_mark': 61, 'min_mark': 48, 'avg_mark': 55.0},
#     {'name': 'Emma', 'marks': [91, 88, 94, 90, 93], 'max_mark': 94, 'min_mark': 88, 'avg_mark': 91.2}
# ]

for student in students:
    marks = student["marks"]

    student["max_mark"] = max(marks)
    student["min_mark"] = min(marks)
    student["avg_mark"] = sum(marks) / len(marks)
# print(students)


top_student = students[0]
for student in students:
    if student["avg_mark"] > top_student["avg_mark"]:
        top_student = student

print(top_student)

print(f"{top_student["name"]} has a top average of {top_student['avg_mark']}%")




