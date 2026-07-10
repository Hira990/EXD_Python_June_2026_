import re

import re

text = "Please reach out to support@example.com or john.doe123@company.co.uk for help."

# Regex pattern without boundary anchors
email_extract_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

# Find all matches
found_emails = re.findall(email_extract_pattern, text)
print(found_emails)

for email in found_emails:
    text = text.replace(email, 'XXX')

print(text)