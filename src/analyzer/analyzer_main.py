import json

def analyzerMain():
    timerelatedWords = ["after", "afternoon", "afterwards", "alarm clock", "annual", "ante meridian", "anytime", "autumn", "autumnal equinox", "bedtime", "before", "before hand", "belated", "bell", "bicentennial", "biennial", "calendar", "century", "chronological", "chronology", "day", "daylight", "daytime", "decadedecennium", "delay", "delayed", "dial", "early", "eon", "epoch", "equinox", "era", "evening", "everyday", "fall", "fortnight", "future", "gnomon", "high noon", "horology", "hour", "hourglass", "jiffy", "jubilee", "late", "later", "meridian", "midafternoon", "midmorning", "midnight", "millennium", "millisecond", "minute", "moment", "momentarily", "month", "morning", "night", "nighttime", "noon", "now", "o'clock", "overtime", "past", "period", "post meridian", "premature", "present", "prime meridian", "punctual", "quarter hour", "quaver", "schedule", "season", "semester", "semi", "shift", "sidereal time", "solstice", "someday", "sometime", "soon", "spring", "summer", "sundial", "sunrise", "sunset", "synchronized", "tardy", "tempo", "then", "time", "timekeeper", "timepiece", "timer", "timetable", "today", "tomorrow", "tonight", "triennium", "trimester", "twilight", "vernal equinox", "week", "winter", "year", "yesterday", "yesteryear"]
    target = "../../docs/carianArchiveTrans.json"

    with open(target) as file:
        carianArchive = json.load(file)

    timerelatedItems = findTimerelatedItems(carianArchive, timerelatedWords)

    with open("../../docs/carianArchiveTimerelated.json", 'w') as outfile:
        json.dump(timerelatedItems, outfile, indent=2)

def findTimerelatedItems(json, timerelatedWords):
    foundItems = []
    for category in json:
        for item in category['items']:
            isTimerelated = False
            for sentence in item['contentTagged']:
                for word in sentence:
                    if word[0] in timerelatedWords:
                        isTimerelated = True
            if isTimerelated:
                foundItems.append({
                    'itemName' : item['itemName'],
                    'content' : item['content']
                })
                    
    return foundItems

analyzerMain()