email_addresses = [
    "alex91@gmail.com",
    "emma23@yahoo.com",
    "liam77@outlook.com",
    "olivia15@hotmail.com",
    "noah88@icloud.com",
    "ava42@proton.me",
    "ethan19@gmx.com",
    "mia54@aol.com",
    "lucas31@zoho.com",
    "sophia67@mail.com",
    "james92@gmail.com",
    "isabella13@yahoo.com",
    "benjamin84@outlook.com",
    "charlotte25@hotmail.com",
    "henry39@icloud.com",
    "amelia58@proton.me",
    "daniel71@gmx.com",
    "jack83@zoho.com",
    "evelyn29@mail.com",
    "matthew47@gmail.com",
    "abigail65@yahoo.com",
    "sebastian12@outlook.com",
    "ella98@hotmail.com",
    "owen37@icloud.com",
    "scarlett44@proton.me",
    "logan56@gmx.com",
    "grace73@aol.com",
    "david21@gmail.com",
    "lily90@mail.com",
]

# TODO: Clean the list of email address

print(f"Total Emails: {len(email_addresses)}")

def extract_provider_from_email(email):
    """
    function to extract provider from email
    """
    return email.split("@")[1].split(".")[0]

# Create a dictionary with providers as key with count as 0
providers_count = {}
for email in email_addresses:
    provider = extract_provider_from_email(email)
    providers_count[provider] = 0
# print(providers_count)

# Update providers count in dict: providers_count
for email in email_addresses:
    provider = extract_provider_from_email(email)
    providers_count[provider] += 1
print(providers_count)

most_used = max(providers_count, key=providers_count.get)
print(f"Most Used Provider: {most_used}\n")
print(f"{most_used} Emails:\n")
for email in email_addresses:
    provider = extract_provider_from_email(email)
    if provider == most_used:
        print(email)

search_term = input("Search Provider: ")

print("Results:")
for email in email_addresses:
    provider = extract_provider_from_email(email)
    if provider == search_term:
        print(email)