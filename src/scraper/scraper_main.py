import csv
from finder import findAllLinks
from scraper import scraper

def scraperMain():
    relItemsTable = [
        "https://eldenring.wiki.fextralife.com/Daggers",
        "https://eldenring.wiki.fextralife.com/Straight+Swords",
        "https://eldenring.wiki.fextralife.com/Greatswords",
        "https://eldenring.wiki.fextralife.com/Colossal+Swords",
        "https://eldenring.wiki.fextralife.com/Thrusting+Swords",
        "https://eldenring.wiki.fextralife.com/Thrusting+Swords",
        "https://eldenring.wiki.fextralife.com/Curved+Swords",
        "https://eldenring.wiki.fextralife.com/Curved+Greatswords",
        "https://eldenring.wiki.fextralife.com/Katanas",
        "https://eldenring.wiki.fextralife.com/Twinblades",
        "https://eldenring.wiki.fextralife.com/Axes",
        "https://eldenring.wiki.fextralife.com/Greataxes",
        "https://eldenring.wiki.fextralife.com/Hammers",
        "https://eldenring.wiki.fextralife.com/Flails",
        "https://eldenring.wiki.fextralife.com/Great+Hammers",
        "https://eldenring.wiki.fextralife.com/Colossal+Weapons",
        "https://eldenring.wiki.fextralife.com/Spears",
        "https://eldenring.wiki.fextralife.com/Great+Spears",
        "https://eldenring.wiki.fextralife.com/Halberds",
        "https://eldenring.wiki.fextralife.com/Reapers",
        "https://eldenring.wiki.fextralife.com/Whips",
        "https://eldenring.wiki.fextralife.com/Fists",
        "https://eldenring.wiki.fextralife.com/Claws",
        "https://eldenring.wiki.fextralife.com/Light+Bows",
        "https://eldenring.wiki.fextralife.com/Bows",
        "https://eldenring.wiki.fextralife.com/Greatbows",
        "https://eldenring.wiki.fextralife.com/Crossbows",
        "https://eldenring.wiki.fextralife.com/Ballistas",
        "https://eldenring.wiki.fextralife.com/Glintstone+Staffs",
        "https://eldenring.wiki.fextralife.com/Sacred+Seals",
        "https://eldenring.wiki.fextralife.com/Torches",
        "https://eldenring.wiki.fextralife.com/Helms",
        "https://eldenring.wiki.fextralife.com/Chest+Armor",
        "https://eldenring.wiki.fextralife.com/Gauntlets",
        "https://eldenring.wiki.fextralife.com/Leg+Armor",
        "https://eldenring.wiki.fextralife.com/Bell+Bearings",
        "https://eldenring.wiki.fextralife.com/Cookbooks",
        "https://eldenring.wiki.fextralife.com/Consumables",
        "https://eldenring.wiki.fextralife.com/Materials",
        "https://eldenring.wiki.fextralife.com/Crystal+Tears",
        "https://eldenring.wiki.fextralife.com/Info+Items",
        "https://eldenring.wiki.fextralife.com/Key+Items",
        "https://eldenring.wiki.fextralife.com/Multiplayer+Items",
        "https://eldenring.wiki.fextralife.com/Remembrance",
        "https://eldenring.wiki.fextralife.com/Tools",
        "https://eldenring.wiki.fextralife.com/Whetblades",
        "https://eldenring.wiki.fextralife.com/Small+Shields",
        "https://eldenring.wiki.fextralife.com/Medium+Shields",
        "https://eldenring.wiki.fextralife.com/GreatShields",
        "https://eldenring.wiki.fextralife.com/Sorceries",
        "https://eldenring.wiki.fextralife.com/Incantations",
        "https://eldenring.wiki.fextralife.com/Arrows+and+Bolts",
        "https://eldenring.wiki.fextralife.com/Upgrade+Materials"
    ]

    relItemsGrid = [
        "https://eldenring.wiki.fextralife.com/Spirit+Ashes",
        "https://eldenring.wiki.fextralife.com/Talismans",
        "https://eldenring.wiki.fextralife.com/Great+Runes",
    ]

    linkListTables = findAllLinks(relItemsTable)
    linkListGrids = findAllLinks(relItemsGrid)

    linkList = linkListTables + linkListGrids

    scraper(linkList, "../docs/descriptions.csv")

scraperMain()
