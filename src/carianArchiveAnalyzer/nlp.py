import json
from wordcloud import WordCloud
from nltk import word_tokenize, WordNetLemmatizer
import matplotlib.pyplot as plt

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
    getComprehensibleText("../../docs/carianArchiveTrans.json")
    
    with open("../../docs/comprehensibleText.txt") as file:
        comprehensibleText = file.read()
    
    lemComprehensibleText(comprehensibleText)

    with open("../../docs/comprehensibleTextLemmed.txt") as file:
        lemmedText = file.read()

    wordCloudShow(lemmedText)


def getComprehensibleText(target="../../docs/carianArchiveTrans.json"):
    with open(target) as file:
        carianArchive = json.load(file)

    relCategories = [
        "AccessoryName.fmg",
        "ArtsName.fmg",
        "GemName.fmg",
        "GoodsName.fmg",
        "ProtectorName.fmg",
        "WeaponName.fmg"
        ]
    
    comprehensibleText = ""
    for category in carianArchive:
        if category['title'] in relCategories:
            categoryItems = category['items']
            for item in categoryItems:
                comprehensibleText = comprehensibleText + item['content'] + "\n"

    saveToFile(comprehensibleText, "../../docs/comprehensibleText.txt")
    return comprehensibleText


def lemComprehensibleText(comprehensibleText="NaN", target="../../docs/comprehensibleTextLemmed.txt"):
    lemma = WordNetLemmatizer()
    words = word_tokenize(comprehensibleText)

    wordsLemmad = []
    for word in words:
        wordsLemmad.append(lemma.lemmatize(word))

    lemmadText = ""
    for wordLemmad in wordsLemmad:
        lemmadText = lemmadText + wordLemmad + " "

    saveToFile(lemmadText, target)
    return lemComprehensibleText


def saveToFile(text="NaN", target="../../docs/comprehensibleText.txt"):
    with open(target, 'w') as file:
        file.write(text)


def wordCloudShow(text="NaN"):
    wordcloud = WordCloud().generate(text)

    plt.figure(figsize = (12, 12))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()


main()