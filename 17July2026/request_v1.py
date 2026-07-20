"""
pip install requests
"""

"""


Status Codes:
- 201 Created
- 200: OK
- 404: Not Found
- 500: Internal Server Error
"""

import requests

# response = requests.get("http://www.google.com")
#
# print(response.status_code)
# print(response.text)

print("=========================")

response = requests.get("https://dummyjson.com/products")

print(response.status_code)
print(response.json())
if response.status_code == 200:
    print("ok")
    products_in_json = response.json()
    for p in products_in_json['products']:
        print(p['title'])
