import requests
from bs4 import BeautifulSoup


url = "https://www.python.org/jobs?page=1"
response = requests.get(url)
print(response.status_code)
# print(response.text)
html_response = response.text

soup = BeautifulSoup(html_response, 'html.parser')
# print(soup.prettify())

li_items = soup.select("ol.list-recent-jobs.list-row-container.menu > li")

jobs = []
for item in li_items:
    company_span = item.find("span", class_="listing-company-name")
    job_title = company_span.find("a").get_text(strip=True)
    company_name = list(company_span.stripped_strings)[-1]
    print(job_title)
    print(company_name)

    job_type_span = soup.find("span", class_="listing-job-type")
    job_type_a_tags = job_type_span.find_all("a")
    job_tags = []
    for a_tag in job_type_a_tags:
        job_tags.append(a_tag.get_text(strip=True))
    print(job_tags)
    print("--------------")
    job_object = {
        "title": job_title,
        "company": company_name,
        "tags": job_tags
    }
    jobs.append(job_object)

print(jobs)
print(len(jobs))