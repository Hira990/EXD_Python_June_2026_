from pip._internal.commands import search

books = [
    {
        "id": 1,  # use uuid here
        "title": "Python Crash Course",
        "author": "Eric Matthes",
    },
    {
        "id": 2,    # use uuid here
        "title": "Java Crash Course",
        "author": "John Smith",
    },
]

"""
1. Add Book
2. View Books
3. Search Book
7. Exit
"""

# Search books
search_term = "python"
found_book = False
for book in books:
    if search_term.lower() in book["title"].lower():
        print(f"{book["title"]} found...")
        found_book = True
if not found_book:
    print(f"{search_term} not found...")