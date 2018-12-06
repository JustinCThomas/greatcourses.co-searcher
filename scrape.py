import requests
from bs4 import BeautifulSoup

base_url="https://www.greatcourses.co"



# Specify the starting and stopping points for the scraping
def page_range(start=1, stop=start+9):
    full_url = base_url + str(start)
    if start < stop:
        for i in range(start, stop):
            req = requests.get("{0}{1}".format(base_url, i))
            content = req.content

            html_content = BeautifulSoup(content, "html.parser")
