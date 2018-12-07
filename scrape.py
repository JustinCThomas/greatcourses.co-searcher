import requests
from bs4 import BeautifulSoup
from time import sleep

base_url="https://www.greatcourses.co"

# Specify the starting and stopping points for the scraping
def scrape_page_range(start=1, stop=10):
    full_url = base_url + str(start)
    if start <= stop:
        for i in range(start, stop + 1):
            print("Now scraping page %s...\n" % i)
            req = requests.get("{0}/page/{1}".format(base_url, i))
            content = req.content
            soup = BeautifulSoup(content, "html.parser")
            cards = soup.find_all(class_="card")

            free_courses = []
            for i in range(len(cards)):
                if cards[i].find(class_="card-footer").find("b").get_text() == 'FREE':
                    free_courses.append(cards[i])
            for i in free_courses:
                print(i.find(class_="card-title").find("b").get_text())
                print(base_url + i.find(class_="card-footer").find("a")["href"])
                print()
            print()
            sleep(1)


if __name__ == "__main__":
    page_start = input("Enter the starting page number: ")
    page_end = input("Enter the ending page number: ")
    print()

    try:
        if page_start == '' or page_end == '':
            print("Using the default page settings: 1-10.")
            scrape_page_range()
        else:
            print("MANUAL")
            scrape_page_range(int(page_start), int(page_end))
    except Exception as e:
        print("Something went wrong.\nBe sure to enter integers for the page numbers.")
        print(e)
