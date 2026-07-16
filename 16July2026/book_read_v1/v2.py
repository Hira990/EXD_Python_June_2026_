from pypdf import PdfReader

reader = PdfReader("image-in-pdf.pdf")

print(reader)

number_of_pages = len(reader.pages)
print(f"Number of pages: {number_of_pages}")

full_book_text = ""
for page in reader.pages:
    text = page.extract_text()
    full_book_text = full_book_text + text

print(full_book_text)

"""
need ocr for the text to read from the image
"""
