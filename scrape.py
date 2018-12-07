import requests
from bs4 import BeautifulSoup
from time import sleep

base_url="https://www.greatcourses.co"

# Specify the starting and stopping points for the scraping
def scrape_page_range(start=1, stop=10):
    full_url = base_url + str(start)
    if start < stop:
        for i in range(start, stop + 1):
            req = requests.get("{0}/page/{1}".format(base_url, i))
            content = req.content
            soup = BeautifulSoup(content, "html.parser")
            print(i)
            sleep(1)


if __name__ == "__main__":
    page_start = input("Enter the starting page number: ")
    page_end = input("Enter the ending page number: ")

    try:
        if page_start == '' or page_end == '':
            print("EMPTY!")
            scrape_page_range()
        else:
            print("MANUAL")
            scrape_page_range(int(page_start), int(page_end))
    except:
        print("Something went wrong.\nBe sure to enter integers for the page numbers")
