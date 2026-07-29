from bs4 import BeautifulSoup

url = "https://books.toscrape.com"

"""
Extract all books (products from this website) with the following information
- Book Title
- Category
- Image URL
- Price
- In Stock or Not
- No of Available books in Stock
- No of Stars in Review (Visual Star Reviews)
- Description
- UPC
"""