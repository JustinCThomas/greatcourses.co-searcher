import requests
from bs4 import BeautifulSoup

base_url="https://www.greatcourses.co"


page_start = input("Enter the starting page number: ")
page_end = input("Enter the ending page number: ")

try:
    if page_start == '' || page_end == '':
        page_range()
    else:
        page_range(int(page_start), int(page_end))
except:
    print("Something went wrong.\n Be sure to enter integers for the page numbers")


# Specify the starting and stopping points for the scraping
def page_range(start=1, stop=start+9):
    full_url = base_url + str(start)
    if start < stop:
        for i in range(start, stop):
            req = requests.get("{0}/page/{1}".format(base_url, i))
            content = req.content

            html_content = BeautifulSoup(content, "html.parser")
