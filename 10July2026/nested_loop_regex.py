import re

posts = [
    "I love Python! #Python #Coding",
    """
    This post has
    DSGWE
    DSB
    no hashtags.""",
    "Learning regex is fun. #Regex",
    "Another plain post.",
    "#AI is changing the world! #MachineLearning",
    34546789
]

hashtags_full_list = []
for post in posts:
    # post = str(post)  # In case we get something other than str
    if isinstance(post, str):
        hashtags = re.findall(r"#(\w+)", post)
        print(hashtags)
        for hashtag in hashtags:
            hashtags_full_list.append(hashtag)
    else:
        print(f"skipping: {post}")

print(hashtags_full_list)

