import time
import csv
import os
from bs4 import BeautifulSoup
from selenium import webdriver
import requests

# url to scrape data from
target_url = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

# getting the chromedriver
# browser = webdriver.Chrome(os.getcwd()+"\\chromedriver.exe")
# browser.get(target_url)
stars_list=[]
headers = ['Name','Distance','Mass','Radius']
def scrape():
    html_page = requests.get(target_url)
    soup = BeautifulSoup(html_page.content,"html.parser")
    table_content :soup = soup.select('#mw-content-text > div.mw-parser-output > table:nth-child(14) > tbody')[0]
    tr:soup
    # print(soup)
    with open('soup.html','w',encoding='utf-8') as f:
        f.write(str(table_content))
        f.close()
    for tr in table_content.find_all('tr')[1:]:
        td:soup
        # print(tr)
        i=0
        temp_list=[]
        for td in tr.find_all('td'):
            #star name, radius, mass and distance data
            #Name
            if i==0 and len(td.find_all('a'))>0:
                a:soup=td.find_all('a')[0]
                temp_list.append(str(a.contents[0]))
            #radius
            if i==9:
                c= td.contents
                if len(c)>0:
                    temp_list.append(str(c[0]))
                else:
                    temp_list.append('NAN')
            #mass
            if i==8:
                c= td.contents
                if len(c)>0:
                    temp_list.append(str(c[0]))
                else:
                    temp_list.append('-')
            #distance light years
            if i==5:
                c= td.contents
                if len(c)>0:
                    temp_list.append(str(c[0]))
                else:
                    temp_list.append('NAN')
            i+=1
        stars_list.append(temp_list)
        

if __name__ =="__main__":
    scrape()
    # print(stars_list)
    with open("drawf_stars.csv","w",encoding="utf-8",newline='') as f:
            w = csv.writer(f)
            w.writerow(headers)
            w.writerows(stars_list)
            f.close()