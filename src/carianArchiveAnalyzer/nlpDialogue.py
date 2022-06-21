import json
import re
from nlpItemDescriptions import getComprehensibleText, tagComprehensibleText

# Categories:
# [ ] AccessoryName.fmg
# [ ] ArtsName.fmg
# [ ] EventTextForMap.fmg
# [ ] GemName.fmg
# [ ] GoodsName.fmg
# [ ] NpcName.fmg
# [ ] PlaceName.fmg
# [ ] ProtectorName.fmg
# [x] TalkMsg.fmg
# [ ] TutorialTitle.fmg
# [ ] WeaponEffect.fmg
# [ ] WeaponInfo.fmg
# [ ] WeaponName.fmg

def nlpDialogueMain():
    relCategories = [
        "TalkMsg.fmg"
        ]
    
    with open("../../docs/carianArchiveTrans.json") as file:
        carianArchive = json.load(file)

    comprehensibleText = getComprehensibleText(carianArchive, relCategories)
    comprehensibleTextRestructured = restructureDialogue(comprehensibleText)
    comprehensibleTextStripped = stripComprehensibleText(comprehensibleTextRestructured)
    taggedItems = tagComprehensibleText(comprehensibleTextStripped)
    jsonOut = addToJson(carianArchive, taggedItems, relCategories)

    with open("../../docs/carianArchiveTrans.json", 'w') as outfile:
        json.dump(jsonOut, outfile, indent=2)

def restructureDialogue(comprehensibleText):
    newItems = []
    foundItems = ""
    newItemName = ""
    for index, item in enumerate(comprehensibleText):
        if item[0] != '[na]':
            newItemName = item[0]
            foundItems = item[1]
        else:
            foundItems = foundItems + item[1]
        
        length = len(comprehensibleText) - 1
        if index < length:
            nextItem = comprehensibleText[index + 1]
            if nextItem[0] != '[na]':
                newItems.append([newItemName, foundItems])
                newItemName = ""
                foundItems = []
        else:
            newItems.append([newItemName, foundItems])
    
    return newItems

def stripComprehensibleText(comprehensibleText):
    newComprehensibleText = []
    for item in comprehensibleText:
        replacedBraces = re.sub(' \[.+?\] ', " ", item[1])
        newComprehensibleText.append([item[0], replacedBraces])

    return newComprehensibleText

def addToJson(json, taggedItems, relCategories):
    newCategory=[]
    for taggeditem in taggedItems:
        newCategory.append({
            'itemName' : taggeditem[0],
            'content' : taggeditem[1]
        })

    newJson = []
    for category in json:
        if category['title'] in relCategories:
            newJson.append({
                'title' : category['title'],
                'items' : newCategory
            })
        else:
            newJson.append(category)

    return newJson
