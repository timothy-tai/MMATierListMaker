import requests
from bs4 import BeautifulSoup

# Gets all of the fighter page links from page - returns list of links
def getLinks(fighterPageURL: str):
    fighterPageHTML = requests.get(fighterPageURL)
    fighterPageHTMLContent = BeautifulSoup(fighterPageHTML.content, 'html.parser')
    listofFighterURLs = []
    for link in fighterPageHTMLContent.find_all('a', class_ = 'b-link b-link_style_black', href=True):
        if link['href'] not in listofFighterURLs:
            listofFighterURLs.append(link['href'])
    return listofFighterURLs

# Gets the fighters stats using BeautifulSoup
def getFighter(fighterURL: str):
    page = requests.get(fighterURL)
    pageContent = BeautifulSoup(page.content, 'html.parser')
    name = pageContent.find('span', class_ = 'b-content__title-highlight')
    name = name.text.strip()
    nickname = pageContent.find('p', class_ ='b-content__Nickname')
    nickname = nickname.text.strip()
    if(nickname == ''):
        nickname = 'N/A'
    record = pageContent.find('span', class_ = 'b-content__title-record')
    record = record.get_text(separator=" ", strip=True)
    record = record.split()
    record = record[1]
    stats = pageContent.find('div', class_='b-list__info-box b-list__info-box_style_small-width js-guide')
    statsList = []
    for thing in stats.find_all('li', class_="b-list__box-list-item b-list__box-list-item_type_block"):
        temp = thing.get_text(separator=" ", strip=True)
        tempList = temp.split()
        statsList.append(tempList)
    if(statsList[0][1] == '--'):
        height = 'N/A'
    else:
        height = statsList[0][1] + statsList[0][2]
    if(statsList[1][1] == '--'):
        weight = 'N/A'
    else:
        weight = statsList[1][1] + ' lbs'
    if(statsList[2][1] == '--'):
        reach = 'N/A'
    else:
        reach = statsList[2][1]
    if(len(statsList[3]) != 2):
        stance = 'N/A'
    else:
        stance = statsList[3][1]
    if(statsList[4][1] == '--'):
        dob = 'N/A'
    else:
        dob = statsList[4][1] + ' ' + statsList[4][2] + ' ' + statsList[4][3]
    
    fighterStats = [name, nickname, record, height, weight, reach, stance, dob]
    return fighterStats


