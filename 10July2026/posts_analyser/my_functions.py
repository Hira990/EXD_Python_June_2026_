import re

def extract_hashtags(post):
    if isinstance(post, str):
        hashtags = re.findall(r"#(\w+)", post)
        return hashtags
    else:
        return []