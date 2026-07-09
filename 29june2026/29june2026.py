import random

original_list = ["Alice", "Bob", "Charlie", "David", "Emma", "Frank", "Grace", "Henry", "Isabella", "Jack", "Katherine", "Liam", "Mia", "Noah", "Olivia", "Peter", "Quinn", "Ryan", "Sophia", "Thomas"]
max_index = len(original_list) - 1

for index, value in enumerate(original_list):
    patient_dict = {
        "name": value,
        "index": index
    }
    original_list[index] = patient_dict

# print(len(original_list))
# random_numbers = []

mid_index_value = int(len(original_list)/2)
random_index_list = []
for i in range(0, mid_index_value):
    random_number = random.randint(0, max_index)
    print(random_number)
    random_index_list.append(random_number)

print(random_index_list)


unique_random_index_list = list(set(random_index_list))
print(unique_random_index_list)

print(len(random_index_list))
print(len(unique_random_index_list))

number_of_random_numbers_shorted = len(random_index_list) - len(unique_random_index_list)

for i in range(0, number_of_random_numbers_shorted - 1):
    random_number = random.randint(0, max_index)




#
# # Random 20 names list
# # Get the random 10 names from the above list
# # 10 to 5 and then 1 name
#
# # Also print the index of the final name (index from the original_list)
#
# original_list = ["a", "b", "c", "d", "e", "f"]
# original_list_with_dict = [
#     {"name": "Alice", "index": 0},
#     "Bob"]
#
#
# final_name = "c"
# final_name_index = 2
#
#
# names = ["iftikhar", "ali"]
# names = [("iftikhar", "o+Ve"), "ali"]
# # print(names[0][1])
# # names = ["iftikhar", "o+ve", "ali", "b+ve"]
# # print("testing")
#
#
#
# my_dict = {
#     "name": "Alice",
# }
# my_dict["index"] = 0
# my_dict["index"] = 1
# print(my_dict)
# my_dict = {
#     "name": "Alice",
#     "index": 0
# }
# print(my_dict)


# my_list = ["asd", "asa", "asfa"]
# my_list[0] = "dscdwvd"
# print(my_list)


numbers  = [1, 2, 3,45 , 5464]
new_number = 3
if new_number in numbers:
    print("alreadt pra hua ha")



# a= 200
# while a > 5:
#     print("test")
#     a = a -1