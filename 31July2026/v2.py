# Read the file student.xml

# convert it to json and show all the info

student = {
    "name": "iftikhar",
    "email": "iftikhar@gmail.com",
    "add": "lahore"
}
print(student.items())

for key, value in student.items():
    print(f"{key}: {value}")