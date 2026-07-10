import email
import re

emails = [
    "ali@gmail.com",
    "john.smith@yahoo.com",
    "invalid-email",
    "abc@",
    "admin@company.co.uk",
    "test@gmail"
]

email_extract_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

for email in emails:
    email_matched = re.search(email_extract_pattern, email)
    if email_matched:
        print(f"{email} -> Valid")
    else:
        print(f"{email} -> Invalid")