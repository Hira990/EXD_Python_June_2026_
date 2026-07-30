import requests

url = "http://127.0.0.1:8000/get-jobs-by-category?category=manager-executive"

response = requests.get(url)

if response.status_code == 200:
    json_response = response.json()
    for j in json_response["jobs"]:
        pass
else:
    jobs = []