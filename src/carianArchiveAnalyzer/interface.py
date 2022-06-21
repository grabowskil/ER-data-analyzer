from bs4 import BeautifulSoup
import re
import json

def transformCarianArchive(
        target="../../docs/CarianArchive.html",
        transformedCarianArchiveFile="../../docs/carianArchiveTrans.json"
    ):
    findAllCategories(target, transformedCarianArchiveFile)

def findAllCategories(target="../../docs/CarianArchive.html", transformedCarianArchiveFile="../../docs/carianArchiveTrans.json"):
    with open(target) as openFile:
        soup = BeautifulSoup(openFile, 'html.parser')

    categories = soup.select('div')

    foundCategories = []
    for category in categories:
        categoryTitle = category.get('id')

        foundItems = []
        categoryItems = category.find_all('h3')
        for item in categoryItems:

            categoryItemNo, categoryItemName = categoryItemSplitter(item.contents)
            content = contentFinder(item)

            foundItems.append({
                'itemNo' : categoryItemNo,
                'itemName' : categoryItemName,
                'content' : content
            })

            
        
        foundCategories.append({
            'title' : categoryTitle,
            'items' : foundItems
        })

    with open(transformedCarianArchiveFile, 'w') as outfile:
        json.dump(foundCategories, outfile, indent=2)

def categoryItemSplitter(categoryItem="['Bone Ballista Bolt [53030000]']"):
    categoryItemStr = categoryItem[0]
    categoryItemNo = useRegex(categoryItemStr, '\\[.*\\]').translate({ord(ch):'' for ch in '[]'})
    categoryItemName = useRegex(categoryItemStr, "[a-zA-Z ':-]+[a-zA-Z]")
    
    return categoryItemNo, categoryItemName

def contentFinder(item):
    foundContent = ""
    if item is not None:
        for sibling in item.next_siblings:
            if sibling.name != "h3":
                text = sibling.text
                text = text.strip()
                text = text.strip('\n')
                text = text.replace("\n        ", " ")

                length = len(foundContent)
                if length > 0:
                    if foundContent[length - 1] != " ":
                        foundContent = foundContent + " " + text
                    else:
                        foundContent = foundContent + text
                else:
                    foundContent = foundContent + text
            else:
                break

    return foundContent

def useRegex(input="Bone Ballista Bolt [53030000]", pattern='\\[.*\\]'):
    group = re.search(pattern, input)
    if group is not None:
        return group.group(0)
    else:
        return "[na]"


transformCarianArchive()