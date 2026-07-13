# age = 200000
# # print(age)
#
# # print(age/0)
#
#
# try:
#     name = "Iftikhar"
#     age = 0
#     print(name + age)
# except:
#     print("errrooor")
#
#
# print("this is end")
import traceback

# =========================================


name = "Chaudhry Iftikhar Hussain"
age = str(29)

try:
    # print(f"Name: {name}, Age: {age}")
    print(8/0)
    print(8)
    print("Name: " + name + ", Age: " + age)
except NameError:
    print("name error")
except TypeError as e:
    print("type error")
except Exception as e:
    traceback.print_exc()
else:
    print("ok")
finally:
    print("code executed successfully")

print("program started")