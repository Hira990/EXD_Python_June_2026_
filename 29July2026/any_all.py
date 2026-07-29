marks = [34, 67, 93, 67, 99, 100]
least_one_failed = any([m < 50 for m in marks])
print(marks)
print(least_one_failed)

all_passed = all([m > 50 for m in marks])
print(marks)
print(all_passed)


# # Check if any of the student is failed with marks less than 50
# least_one_failed = False
# for mark in marks:
#     if mark < 50:
#         least_one_failed = True
#         break
# print("least one failed" if least_one_failed else "all passed")



