"""Support: Gmail, Yahoo, .com, .pk, .co.uk"""
import re

emails = [
    "ali@gmail.com",
    "john.smith@yahoo.com",
    "invalid-email",
    "abc@",
    "admin@company.co.uk",
    "test@outlook.com"
]

email_extract_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

for email in emails:
    email_matched = re.search(email_extract_pattern, email)
    if email_matched:
        print(f"{email} -> Valid")
        # if not "outlook" in email:
        #     print(f"{email} -> Valid")
        # else:
        #     print(f"{email} -> Invalid")
    else:
        print(f"{email} -> Invalid")