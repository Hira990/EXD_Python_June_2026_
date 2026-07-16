from pypdf import PdfReader

reader = PdfReader("crime-and-punishment-by-fyodor-dostoevsky.pdf")

print(reader)

number_of_pages = len(reader.pages)
print(f"Number of pages: {number_of_pages}")

# full_book_text = ""
# for page in reader.pages:
#     page_text = page.extract_text()
#     full_book_text = full_book_text + page_text

full_book_text = ""
for i in range(0, 5):
    print(i)
    page_object = reader.pages[i]
    page_text = page_object.extract_text()
    full_book_text = full_book_text + page_text

print(full_book_text)

why_count = 0
words_list = full_book_text.split()
for word in words_list:
    if word.lower() == "he":
        why_count += 1

print(why_count)

"""
pypdf
easyocr
"""
