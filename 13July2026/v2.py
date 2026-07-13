import re

def get_posts_from_db():
    posts = [
        "I love Python! #Python #Coding",
        """
        This post has
        DSGWE
        DSB
        no hashtags.""",
        34546789,
        "Learning regex is fun. #Regex",
        "Another plain post.",
        "#AI is changing the world! #MachineLearning",

    ]
    if len(posts) == 0:
        return None
    return posts

hashtags_full_list = []

posts = get_posts_from_db()
for post in posts:
    try:
        hashtags = re.findall(r"#(\w+)", post)
        for hashtag in hashtags:
            hashtags_full_list.append(hashtag)
    except Exception as e:
        print(f"skipping: {post}, Exception: {e}")
    else:
        print("all ok")

print(hashtags_full_list)


# ==================================================

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
    try:
        email_matched = re.search(email_extract_pattern, email)
        if email_matched:
            print(f"{email} -> Valid")
        else:
            print(f"{email} -> Invalid")
    except Exception as e:
        print("Exception occurred: ", e)