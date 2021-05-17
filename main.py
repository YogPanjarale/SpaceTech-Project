import time
import csv
import os
from bs4 import BeautifulSoup
from selenium import webdriver
import requests

# url to scrape data from
target_url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

# getting the chromedriver
# browser = webdriver.Chrome(os.getcwd()+"\\chromedriver.exe")
# browser.get(target_url)
stars_list=[]
headers = ['Name','Distance','Mass','Radius']
def scrape():
    html_page = requests.get(target_url)
    soup = BeautifulSoup(html_page.content,"html.parser")
    table_content :soup = soup.find_all("tbody")[0]
    tr:soup
    for tr in table_content.find_all("tr"):
        td:soup
        i=0
        temp_list=[]
        for td in tr.find_all('td'):
            if i==1 and len(td.find_all('a'))>0:
                a:soup=td.find_all("a")[0]
                temp_list.append(str(a.contents[0]))
            if i==3:
                if "span" in str(td.contents[0]).strip('\n'):
                    temp_list.append(str(td.contents[1]).strip('\n'))
                else:
                    temp_list.append(str(td.contents[0]).strip('\n'))
            if i==5:
                temp_list.append(str(td.contents[0]).strip('\n'))
            if i==6:
                temp_list.append(str(td.contents[0]).strip('\n'))
            i+=1
            # print(td.contents[0])
        if len(temp_list)==4:
            stars_list.append(temp_list)
        

if __name__ =="__main__":
    scrape()
    print(stars_list)
    with open("planet_data.csv","w",encoding="utf-8",newline='') as f:
            w = csv.writer(f)
            w.writerow(headers)
            w.writerows(stars_list)
            f.close()