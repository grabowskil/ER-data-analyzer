import requests
from bs4 import BeautifulSoup
from data import writeRowToCsv, findInCsv

def tableFinder(target="https://eldenring.wiki.fextralife.com/Daggers"):
    response = requests.get(
        url = target
    )
    
    soup = BeautifulSoup(response.content, 'html.parser')

    tables = soup.select('table.wiki_table.sortable.searchable')
    
    links = []

    for table in tables:
        tableBody = table.find('tbody')

        rows = tableBody.find_all('tr')

        for row in rows:
            col = row.find('td')
            if col is not None:
                try:
                    link = col.find('a', attrs={'class':'wiki_link'})['href']
                    links.append(link)
                except:
                    print("Skipped: An exception occured while trying to add " + str(col) + " it was skipped.")

    return links

def gridFinder(target="https://eldenring.wiki.fextralife.com/Spirit+Ashes"):
    response = requests.get(
        url = target
    )

    soup = BeautifulSoup(response.content, 'html.parser')

    grid = soup.find_all('a', attrs={'class:wiki_link'})

    links = []

    for a in grid:
        try:
            link = a['href']
            links.append(link)
        except:
            print("Skipped: An exception occured while trying to add " + str(a) + " it was skipped.")


def findAllLinks(relItems=["https://eldenring.wiki.fextralife.com/Daggers"], target="../docs/linklist.csv", mode='table'):
    linkListComplete = []

    for item in relItems:
        if mode == 'table':
            linkList = tableFinder(item)
        elif mode == 'grid':
            linkList = gridFinder(item)

        for link in linkList:
            
            if link.find("https") == -1:
                link = "https://eldenring.wiki.fextralife.com" + link
            
            if findInCsv(link, target) == False:
                writeRowToCsv([link], target)
                linkListComplete.append([link])
            else:
                print("Skipped: " + link + " already imported.")

    return linkListComplete
