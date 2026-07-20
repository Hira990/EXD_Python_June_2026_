"""

openweathermap.org
newsapi.org

SEE THE ABOVE WEBSITE API DOCS
USE THE REQUEST MODULE IN YOUR CODE TO EXTRACT THE DATA FROM THEIR API

"""

import os
from dotenv import load_dotenv
from newsapi import NewsApiClient

load_dotenv()

"""
pip install python-dotenv
"""



newsapi_apikey = os.getenv("NEWSAPI_APIKEY")
if not newsapi_apikey:
    print("no api key in e.v file")
else:
    # Init
    newsapi = NewsApiClient(api_key=newsapi_apikey)

    # /v2/top-headlines/sources
    sources = newsapi.get_sources()
    print(sources)