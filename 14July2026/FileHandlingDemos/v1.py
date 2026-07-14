# try:
#     # file = open("C:\\Users\\Dream Laptops\\PycharmProjects\\EXD_Python_June_2026\\14July2026\\global_file.txt")
#     # print(file.read())
#     file = open("students.txt")
#     file_content = file.read()
#     print(file_content)
#     print("file read successfully")
# except FileNotFoundError:
#     print("File not found")
# except Exception as e:
#     print(f"Exception: {e}")


try:
    with open("students.txt", "x") as file:
        file.write("\nNow the file has more content!")
except FileNotFoundError:
    print("File not found")
except FileExistsError:
    print("File exists")
except Exception as e:
    print(f"Exception: {e}")
