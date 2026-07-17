"""
https://fakestoreapi.com/docs
"""
import requests, os

url = "https://fakestoreapi.com/products"

response = requests.get(url)

for product in response.json():
    print(product["id"])
    print(product['image'])

    byte_response = requests.get(product['image']).content

    if os.path.exists("product_images1"):
        with open(f'product_images/{product['id']}.jpg', 'wb') as f:
            f.write(byte_response)
        print(f"{product['image']} completed...")



"""
Theory k lie

kahan pe get, post, put, patch, delete, etc use krni hain


main status codes pta honey chahie
200
201 created
404 not found
500 internal server error
422 unprocessable entity
400 bad request

"""