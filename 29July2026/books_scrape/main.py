import requests
from bs4 import BeautifulSoup


page_number = 40

while True:
    url = f"https://books.toscrape.com/catalogue/page-{page_number}.html"
    print(url)

    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")

    products = soup.find_all("article", class_="product_pod")

    for product in products:
        print(product)
        title = product.find("h3").find("a")["title"]
        print(title)
        href = product.select_one("div.image_container a")["href"]
        print(href)
        product_info_url = f"https://books.toscrape.com/catalogue/{href}"
        print(product_info_url)

        response_product_pg = requests.get(product_info_url)
        soup_prod_page = BeautifulSoup(response_product_pg.content, "html.parser")
        # print(soup_prod_page)
        table = soup_prod_page.find("table", class_="table table-striped")
        upc = table.find("th", string="UPC").find_next("td").get_text(strip=True)
        print(upc)

        break




    break

    page_number += 1

    if response.status_code != 200:
        break