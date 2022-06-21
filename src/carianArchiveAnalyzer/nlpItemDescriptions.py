import json
from nltk import sent_tokenize, word_tokenize, pos_tag, WordNetLemmatizer
from nltk.corpus import stopwords as sw
from nltk.corpus import wordnet as wn

# Categories:
# [x] AccessoryName.fmg
# [x] ArtsName.fmg
# [ ] EventTextForMap.fmg
# [x] GemName.fmg
# [x] GoodsName.fmg
# [ ] NpcName.fmg
# [ ] PlaceName.fmg
# [x] ProtectorName.fmg
# [?] TalkMsg.fmg
# [ ] TutorialTitle.fmg
# [ ] WeaponEffect.fmg
# [ ] WeaponInfo.fmg
# [x] WeaponName.fmg

def main():
    with open("../../docs/carianArchiveTrans.json") as file:
        carianArchive = json.load(file)
    
    comprehensibleText = getComprehensibleText(carianArchive)
    taggedItems = tagComprehensibleText(comprehensibleText)
    jsonOut = addToJson(carianArchive, taggedItems)

    with open("../../docs/carianArchiveTrans.json", 'w') as outfile:
        json.dump(jsonOut, outfile, indent=2)


def getComprehensibleText(carianArchive={"title": "na.fmg","items":[]}):
    relCategories = [
        "AccessoryName.fmg",
        "ArtsName.fmg",
        "GemName.fmg",
        "GoodsName.fmg",
        "ProtectorName.fmg",
        "WeaponName.fmg"
        ]

    comprehensibleText = []
    for category in carianArchive:
        if category['title'] in relCategories:
            categoryItems = category['items']
            for item in categoryItems:
                comprehensibleText.append([item['itemName'], item['content']])
    
    return comprehensibleText


def tagComprehensibleText(comprehensibleText=[['Lightning Greatbolt', 'Greatbolt tipped with a clump of Gravel Stone shards. Deals powerful lightning damage. ']]):
    lemma = WordNetLemmatizer()
    stopwords = sw.words('english')

    taggedItems = []
    for item in comprehensibleText:
        sentences = sent_tokenize(item[1])

        processedSentences = []
        for sentence in sentences:
            words = tokenizerWord(sentence)
            taggedWords = pos_tag(words)

            lemmedWords = []
            for word in taggedWords:
                pos = get_wordnet_pos(word[1])
                if pos != '':
                    lemmedWord = lemma.lemmatize(word[0], pos)
                    lemmedWords.append([lemmedWord, pos])
                else:
                    if word[0] in stopwords:
                        pos = "sw"
                    lemmedWords.append([word[0], pos])
            
            processedSentences.append(lemmedWords)

        taggedItems.append([item[0], processedSentences])
    
    return taggedItems
        


def saveToFile(text="na", target="../../docs/comprehensibleText.txt"):
    with open(target, 'w') as file:
        file.write(text)

def tokenizerWord(sentence="na"):
    allWords = word_tokenize(sentence)

    words = []
    for word in allWords:
        if word.isalpha():
            words.append(word.lower())

    return words

def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wn.ADJ
    elif treebank_tag.startswith('V'):
        return wn.VERB
    elif treebank_tag.startswith('N'):
        return wn.NOUN
    elif treebank_tag.startswith('R'):
        return wn.ADV
    else:
        return ''

def addToJson(json, taggedItems):
    newJson = []
    for category in json:
        newItems = []
        for item in category['items']:
            newItem = []
            for taggedItem in taggedItems:
                if item['itemName'] == taggedItem[0]:
                    newItem = [{
                        'itemNo' : item['itemNo'],
                        'itemName' : item['itemName'],
                        'content' : item['content'],
                        'contentTagged' : taggedItem[1]
                    }]
            if newItem == []:
                newItem = category['items']
            newItems.append(newItem)
                
        newJson.append({
            'title' : category['title'],
            'items' : newItems
        })

    return newJson

main()