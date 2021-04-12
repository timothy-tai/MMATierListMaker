from FighterClass import Fighter
from UFCwebscraper import getLinks, getFighter
from pymongo import MongoClient
from string import ascii_lowercase
from configparser import ConfigParser

# Inserts fighter data into MongoDB Atlas database
def main():
    config = ConfigParser()
    config.read('config.ini')
    classFighters = []
    for letter in ascii_lowercase:
        fighterPageURL = "http://ufcstats.com/statistics/fighters?char=" + letter + "&page=all"
        newList = getLinks(fighterPageURL)
        for thing in newList:
            tempStats = getFighter(thing)
            fighter = Fighter(tempStats[0], tempStats[1], tempStats[2],tempStats[3], tempStats[4], tempStats[5], tempStats[6], tempStats[7])
            classFighters.append(fighter)
    client = MongoClient(config.get('dbAccess', 'fighterdb'))
    db = client.get_database('ufc_db')
    fighterRecords = db.fighter_records
    for classInstance in classFighters:
        classInstance.setDict()
        fighterRecords.insert_one(classInstance.getDict())

if __name__ == "__main__":
	main()
