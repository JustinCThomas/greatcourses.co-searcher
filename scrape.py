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

                language = i.find(class_="card-body").find_all("h6")[0].find("b").get_text()
                print("Language: %s" % language)

                language = i.find(class_="card-body").find_all("h6")[1].find("b").get_text()
                print("Category: %s" % language)

                gc_co_url = base_url + i.find(class_="card-footer").find("a")["href"]
                url_split = gc_co_url.split("/")
                course_number = url_split[4]
                udemy_url = "{}/goto/{}".format(base_url, course_number)
                print(udemy_url)
                
                print()
            print()
            sleep(1)


if __name__ == "__main__":
    req = requests.get(base_url)
    content = req.content
    soup = BeautifulSoup(content, "html.parser")

    last_page = int(soup.find(class_="pagination").find_all("li")[5].find("a").get_text())

    scrape_all = input("Do you want to scrape all of the pages?\nThere are %s pages. (y for yes, anything else for no)" % last_page)

    if scrape_all.lower() == 'y':
        scrape_page_range(1, last_page)

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
        print()
        print("Something went wrong.\nBe sure to enter integers for the page numbers.")
        print(e)
