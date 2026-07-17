import requests

domain = "https://catfact.ninja"

url_to_hit = "facts"

parameters = {
    'limit': 4,
    'max_length': 40
}

url = f"{domain}/{url_to_hit}"
# print(url)

response = requests.get(url, params=parameters)

if response.status_code == 200:
    cat_facts = response.json()

    # facts_list = []
    # for f in cat_facts['data']:
    #     facts_list.append(f['fact'])

    facts_list = [f['fact'] for f in cat_facts['data']]
else:
    cat_fact = None

print(facts_list)
print(len(facts_list))
