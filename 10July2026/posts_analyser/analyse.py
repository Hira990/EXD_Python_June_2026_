import re
from data import posts
from my_functions import extract_hashtags

all_hashtags = []
for post in posts:
    this_post_hashtags = extract_hashtags(post)
    for h in this_post_hashtags:
        all_hashtags.append(h)

print(all_hashtags)