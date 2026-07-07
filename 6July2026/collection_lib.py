from collections import Counter

names = [
    "Alice", "Bob", "Charlie", "Alice", "David", "Emma", "Bob", "Frank",
    "Grace", "Hannah", "Isaac", "Jack", "Emma", "Katherine", "Liam",
    "Mia", "Noah", "Olivia", "Peter", "Quinn", "Ryan", "Sophia",
    "Thomas", "Uma", "Victor", "William", "Xavier", "Yasmine", "Zachary",
    "Aaron", "Bella", "Caleb", "Diana", "Ethan", "Faith", "Gabriel",
    "Hazel", "Ian", "Julia", "Kevin", "Lily", "Mason", "Natalie",
    "Owen", "Paisley", "Quentin", "Rose", "Samuel", "Taylor", "Samuel",
    "Uma", "Victor", "William", "Emma", "Xavier", "Yasmine", "Zachary",
    "Alice", "Bella", "Connor", "Delilah", "Elijah", "Freya", "George",
    "Hailey", "Isaiah", "Jasmine", "Kai", "Leah", "Michael", "Nora",
    "Oscar", "Penelope", "Riley", "Scarlett", "Tristan", "Uriel",
    "Vanessa", "Wesley", "Xena", "Yara", "Zane", "Aiden", "Brooklyn",
    "Carson", "Daniel", "Eva", "Finn", "Gianna", "Henry", "Isla",
    "Joshua", "Kennedy", "Logan", "Madison", "Nathan", "Oscar",
    "Patrick", "Ruby", "Alice", "Sophia"
]

counts = Counter(names)
print(counts)
