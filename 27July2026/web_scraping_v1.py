import requests, datetime, json
from bs4 import BeautifulSoup
from pathlib import Path

# Make a directory "jobs" if it does not exist
jobs_folder = Path("jobs")
jobs_folder.mkdir(exist_ok=True)

# extract job code
page_number = 1
jobs = []
while True:

    url = f"https://www.python.org/jobs?page={page_number}"
    response = requests.get(url)
    print(response.status_code)
    if response.status_code != 200:
        print("Error, quiting...")
        break
    # print(response.text)
    html_response = response.text

    soup = BeautifulSoup(html_response, 'html.parser')
    # print(soup.prettify())

    li_items = soup.select("ol.list-recent-jobs.list-row-container.menu > li")

    for item in li_items:
        company_span = item.find("span", class_="listing-company-name")
        job_title = company_span.find("a").get_text(strip=True)
        company_name = list(company_span.stripped_strings)[-1]
        print(job_title)
        print(company_name)

        job_type_span = item.find("span", class_="listing-job-type")
        job_type_a_tags = job_type_span.find_all("a")
        job_tags = []
        for a_tag in job_type_a_tags:
            job_tags.append(a_tag.get_text(strip=True))
        print(job_tags)

        date_posted_span = item.find("span", class_="listing-posted")
        date_posted = date_posted_span.find("time").get_text(strip=True)

        category_span = item.find("span", class_="listing-company-category")
        category = category_span.find("a").get_text(strip=True)

        location_span = item.find("span", class_="listing-location")
        location = location_span.find("a").get_text(strip=True)

        print("--------------")
        job_object = {
            "title": job_title,
            "company": company_name,
            "tags": job_tags,
            "date_posted": date_posted,
            "category": category,
            "location": location
        }
        jobs.append(job_object)

    page_number += 1
    # if page_number > 2:
    #     break

print(jobs)
print(len(jobs))

file_name = f"Jobs_{datetime.datetime.today().strftime("%d_%m_%Y")}.json"
with open(f"jobs/{file_name}", "w") as f:
    json.dump(jobs, f, indent=4)

print("File saved")




