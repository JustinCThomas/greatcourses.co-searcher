import requests
from bs4 import BeautifulSoup
from time import sleep

base_url="https://www.greatcourses.co"

# Specify the starting and stopping points for the scraping
def scrape_page_range(start=1, stop=10, create_file=False):
    full_url = base_url + str(start)
    if create_file:
        file = open("course_information.txt", 'w')

    if start <= stop:
        for i in range(start, stop + 1):
            print("Now scraping page %s...\n" % i)
            req = requests.get("{0}/page/{1}".format(base_url, i))
            content = req.content
            soup = BeautifulSoup(content, "html.parser")
            cards = soup.find_all(class_="card")

            if create_file:
                file.write("PAGE %s\n\n" % i)

            free_courses = []
            for i in range(len(cards)):
                if cards[i].find(class_="card-footer").find("b").get_text() == 'FREE':
                    free_courses.append(cards[i])
            for i in free_courses:
                text_to_write = ""
                print(i.find(class_="card-title").find("b").get_text())
                title = i.find(class_="card-title").find("b").get_text()

                language = i.find(class_="card-body").find_all("h6")[0].find("b").get_text()
                print("Language: %s" % language)

                category = i.find(class_="card-body").find_all("h6")[1].find("b").get_text()
                print("Category: %s" % category)

                gc_co_url = base_url + i.find(class_="card-footer").find("a")["href"]
                url_split = gc_co_url.split("/")
                course_number = url_split[4]
                udemy_url = "{}/goto/{}".format(base_url, course_number)
                print(udemy_url)


                text_to_write = "{}\n{}\n{}\n{}\n\n".format(title, language, category, udemy_url)
                if create_file:
                    file.write(text_to_write)

                print()
            print()
            sleep(1)
        print("Scraping Complete.")


if __name__ == "__main__":
    req = requests.get(base_url)
    content = req.content
    soup = BeautifulSoup(content, "html.parser")

    last_page = int(soup.find(class_="pagination").find_all("li")[5].find("a").get_text())

    scrape_all = input("Do you want to scrape all of the pages?\nThere are %s pages. (y for yes, anything else for no)" % last_page)

    file_output_choice = input("Would you like a file with course information? (y for yes, anything else for no)")
    file_output_choice = True if file_output_choice.lower() == 'y' else False



    if scrape_all.lower() == 'y':
        scrape_page_range(1, last_page, file_output_choice)

    page_start = input("Enter the starting page number: ")
    page_end = input("Enter the ending page number: ")
    print()

    try:
        if page_start == '' or page_end == '':
            print("Using the default page settings: 1-10.")
            scrape_page_range(create_file=file_output_choice)
        else:
            print("MANUAL")
            page_start = 1 if int(page_start) < 1 else page_start
            page_end = last_page if int(page_end) > last_page else page_end
            scrape_page_range(int(page_start), int(page_end), file_output_choice)
    except Exception as e:
        print()
        print("Something went wrong.\nBe sure to enter integers for the page numbers.")
        print(e)
