import requests
from bs4 import BeautifulSoup

base_url="https://www.greatcourses.co"

req = requests.get(base_url)
content = req.content

html_content = BeautifulSoup(c, "html.parser")
