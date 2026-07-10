"""
A company wants to validate employee emails before saving them into the database.

Emails = [
    "ali@gmail.com",
    "john.smith@yahoo.com",
    "invalid-email",
    "abc@",
    "admin@company.co.uk",
    "test@gmail"
]

The function should:
- Accept valid email formats
- Reject invalid emails
- Support:
    Gmail, Yahoo, .com, .pk, .co.uk

Expected Output:
ali@gmail.com -> Valid
john.smith@yahoo.com -> Valid
invalid-email -> Invalid
abc@ -> Invalid

============================================================

A customer support system receives messages containing phone numbers.

message = "
Contact Ali at 0300-1234567.
Backup number is 0321-9876543.
Office: 042-1234567 "

Extract all phone numbers using regex.

[
"0300-1234567",
"0321-9876543",
"042-1234567"
]

============================================================

A website needs strong password validation.

Rules:
Password must contain:
    Minimum 8 characters
    At least one uppercase letter
    At least one lowercase letter
    At least one number
    At least one special character
Test Data:
passwords = [
    "Password123!",
    "hello123",
    "PASSWORD!",
    "Pass@123",
    "abc"
]
Expected:
Password123! Strong
hello123 Weak
PASSWORD! Weak
Pass@123 Strong
abc Weak

============================================================

You are building an Instagram analytics tool.

posts = [
"
Learning Python today.
#python #coding #developer
",

"
My new project is amazing!
#FastAPI #Backend
"
]

Extract all hashtags.

[
"python",
"coding",
"developer",
"FastAPI",
"Backend"
]

============================================================

A crawler collects links from articles.

content = "
Visit our website https://google.com
Documentation:
https://docs.python.org/3/

Contact:
http://example.com/page
"

Extract all links.
https://google.com
https://docs.python.org/3/
http://example.com/page

============================================================

comment = "
This         product is GREAT!!!

I really love it.......
Thank you!!!
"

Using regex:

Remove extra spaces
Remove multiple dots
Remove repeated special characters

This product is GREAT!
I really love it.
Thank you!

============================================================

FastAPI server generates logs:
2026-07-09 10:15:23 INFO User login successful user_id=101
2026-07-09 10:16:10 ERROR Database connection failed
2026-07-09 10:20:45 WARNING Token expired user_id=202

Requirements:

Extract:

Date
Time
Log Level
User ID

Expected:

[
{
"date":"2026-07-09",
"time":"10:15:23",
"level":"INFO",
"user_id":"101"
}
]

============================================================

HR system reads resumes.
resume = "

Name: Ali Ahmed

Email: ali@gmail.com

Phone: 03001234567

Skills:
Python, Django, FastAPI

Experience:
5 years

"

Name
Email
Phone
Skills
Experience

{
"name":"Ali Ahmed",
"email":"ali@gmail.com",
"phone":"03001234567",
"experience":"5 years"
}

============================================================

A company receives invoices as text.

invoice = "

Invoice No: INV-2026-001

Customer:
ABC Pvt Ltd

Amount:
$2500

Date:
09/07/2026

"

{
"invoice":"INV-2026-001",
"customer":"ABC Pvt Ltd",
"amount":"2500",
"date":"09/07/2026"
}

============================================================

Analyze customer support chats.

chat = "

Ali: My order #12345 is delayed.

Support:
Your complaint ID is CMP-9988.

Call us at 03001234567.

"

{
"orders":["12345"],
"complaints":["CMP-9988"],
"phones":["03001234567"]
}


============================================================

Different systems store dates differently.

dates = [
"09-07-2026",
"2026/07/09",
"09 July 2026",
"July 09, 2026"
]

Use regex to identify format, then convert everything into:
2026-07-09

============================================================

Build a Python program that scans a text file and extracts:
Information:

Emails
Phone numbers
URLs
Dates
Hashtags
Currency amounts
IP addresses

Server deployed on 09-07-2026.

Contact:
admin@test.com

Cost:
$1500

Server IP:
192.168.1.10

Visit:
https://example.com

OUTPUT:
{
"emails":["admin@test.com"],
"dates":["09-07-2026"],
"amounts":["1500"],
"ips":["192.168.1.10"],
"urls":["https://example.com"]
}

"""