import requests
from bs4 import BeautifulSoup
from data import writeRowToCsv, findInCsv

def scraper(linkList=[["https://eldenring.wiki.fextralife.com/Dagger"]], target="../docs/descriptions.csv"):
    for link in linkList:
        item = scrapeItem(link[0])

        if findInCsv(item[1], target) == False:
            print("Added: " + str(item[1]) + " added to list.")
            writeRowToCsv(item, target)
        else:
            print("Skipped: " + str(item[1]) + " already in list.")


def scrapeItem(target="https://eldenring.wiki.fextralife.com/Dagger"):
    response = requests.get(
        url = target
    )
    
    soup = BeautifulSoup(response.content, 'html.parser')

    titleSoup = soup.find(id="page-title")
    title = titlestripper(titleSoup.contents[0])

    categories = soup.find(id="breadcrumbs-container").find_all("a")
    categorization = categorystripper(categories)
    
    lineleftEms = soup.find(id="wiki-content-block").select("div.lineleft:has(p em)")
    description = descriptionstripper(lineleftEms)
    
    return [categorization, title, description]
    
def titlestripper(title="none"):
    if title.find(" |") == -1:
        return title

    else:
        return title.split(" |")[0]

def categorystripper(categories):
    categorization = []

    for link in categories:
        category = link.contents[0]
        if category != '+':
            categorization.append(link.contents[0])

    categorizationString = ""
    for category in categorization:
        if categorizationString == "":
            categorizationString = str(category)
        else:
            categorizationString = categorizationString + ", " + str(category)
        

    return categorizationString

def descriptionstripper(lineleftEmDivs):
    description = ""
    for lineleftEmDiv in lineleftEmDivs:
        ems = lineleftEmDiv.find_all("em")
        for em in ems:
            try:
                description = description + str(em.contents[0]) + " "
            except:
                description = description + "ERROR: em not readable"

    if description.find("\xa0"):
        description = description.replace(u'\xa0', u' ')
    
    return description
