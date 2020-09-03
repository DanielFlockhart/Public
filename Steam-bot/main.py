'''
Daniel Flockhart - Discord Steam sale bot
'''
import time, math, random,bs4,requests,os,re
from datetime import datetime
from bs4 import BeautifulSoup
class sales:
    def __init__(self):
        self.url = "https://store.steampowered.com/search/?category1=998&os=win&specials=1"
    def get_data(self):
        r=requests.get(self.url)
        soup=bs4.BeautifulSoup(r.text, "lxml")
        game=str(soup.find_all('div',{'class':'responsive_search_name_combined'})[0].find('span').text)
        file = open("games.txt", "w")
        for i in range(100):
            try:
                game=str(soup.find_all('div',{'class':'responsive_search_name_combined'})[i].find('span').text)
                discount=str(soup.find_all('div',{'class':'col search_discount responsive_secondrow'})[i].find('span').text)
                cost=str(soup.find_all('div',{'class':'col search_price discounted responsive_secondrow'})[i].text)
                # Short ones glitch it 
                prev_cost = cost[2:7]
                new_cost = cost[7:14]
                line = "The game " + game + " is on sale!, It is on a " + discount + " and now costs " + new_cost + ", it used to cost £" + prev_cost
                print(line)
                file.write(line+"\n")
            except:
                pass
        file.close()
            
games = sales()
games.get_data()
