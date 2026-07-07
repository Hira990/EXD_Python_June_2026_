website_logs = [
    {'ip_address': '192.168.1.10', 'page_url': '/about', 'status_code': 200, 'response_time_ms': 123},
    {'ip_address': '203.0.113.15', 'page_url': '/about', 'status_code': 200, 'response_time_ms': 87},
    {'ip_address': '198.51.100.22', 'page_url': '/login', 'status_code': 302, 'response_time_ms': 54},
    {'ip_address': '172.16.5.3', 'page_url': '/login', 'status_code': 401, 'response_time_ms': 63},
    {'ip_address': '8.8.8.8', 'page_url': '/search?q=phone', 'status_code': 200, 'response_time_ms': 201},
    {'ip_address': '1.1.1.1', 'page_url': '/products', 'status_code': 200, 'response_time_ms': 145},
    {'ip_address': '203.0.113.21', 'page_url': '/cart', 'status_code': 200, 'response_time_ms': 110},
    {'ip_address': '198.51.100.31', 'page_url': '/checkout', 'status_code': 500, 'response_time_ms': 782},
    {'ip_address': '10.0.0.2', 'page_url': '/api/users', 'status_code': 200, 'response_time_ms': 42},
    {'ip_address': '172.20.10.4', 'page_url': '/contact', 'status_code': 200, 'response_time_ms': 95},
    {'ip_address': '192.168.1.11', 'page_url': '/products/1', 'status_code': 200, 'response_time_ms': 132},
    {'ip_address': '203.0.113.16', 'page_url': '/products/2', 'status_code': 404, 'response_time_ms': 36},
    {'ip_address': '198.51.100.23', 'page_url': '/blog', 'status_code': 200, 'response_time_ms': 189},
    {'ip_address': '172.16.5.4', 'page_url': '/blog/python', 'status_code': 200, 'response_time_ms': 156},
    {'ip_address': '8.8.4.4', 'page_url': '/settings', 'status_code': 403, 'response_time_ms': 70},
    {'ip_address': '9.9.9.9', 'page_url': '/profile', 'status_code': 200, 'response_time_ms': 98},
    {'ip_address': '192.0.2.1', 'page_url': '/register', 'status_code': 201, 'response_time_ms': 164},
    {'ip_address': '198.18.0.1', 'page_url': '/logout', 'status_code': 204, 'response_time_ms': 44},
    {'ip_address': '203.0.113.40', 'page_url': '/favicon.ico', 'status_code': 404, 'response_time_ms': 18},
    {'ip_address': '198.51.100.40', 'page_url': '/images/logo.png', 'status_code': 200, 'response_time_ms': 25},
]

# Print all IP addresses
# Loop through the list and print only the ip_address field.
# Print only successful requests, status code is 200
# Count how many logs have a status code of 200.
# Count failed requests (Status Code 500)
# Count how many logs have status codes 400 or higher.
# Find the slowest request
# Print the log with the highest response_time_ms.
# Find the fastest request
# Print the log with the lowest response_time_ms.
# Calculate the average response time
# Find the average of all response_time_ms values.
# Print all unique page URLs
# Count visits per page

"""
Produce a dictionary like:
{
    "/": 12,
    "/login": 7,
    "/products": 18
}
"""
urls = []
for log in website_logs:
    urls.append(log["page_url"])
print(urls)

urls_count = {}
for url in urls:
    urls_count[url] = 0
print(urls_count)

for url in urls:
    urls_count[url] += 1

print(urls_count)

"""
Produce a dictionary like:
{
    200: 68, OK
    404: 12, Not Found
    500: 4, Server Error
}
"""

from collections import Counter
