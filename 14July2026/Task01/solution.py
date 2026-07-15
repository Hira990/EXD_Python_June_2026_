# 3

from collections import Counter

users = []
with open("server_logs.txt", "r") as file:
    for line in file:
        if "user=" in line:
            user_name = line.split("user=")[1]
            user_name = user_name.split()[0]
            users.append(user_name)

print(users)
users_counts = Counter(users)
print(users_counts)
print(users_counts.most_common())


if users_counts.most_common()[0][0] == "unknown":
    most_repeated_user = users_counts.most_common()[1][0]
    print(most_repeated_user)