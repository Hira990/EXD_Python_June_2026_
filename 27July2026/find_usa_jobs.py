# Find USA Jobs From the List
import json

with open('jobs/Jobs_27_07_2026.json') as f:
    jobs = json.load(f)

for job in jobs:
    print(job['location'])
    if "United States" in job['location'] or "USA" in job['location'] or "US" in job['location']:
        print("ye ha usa wali")