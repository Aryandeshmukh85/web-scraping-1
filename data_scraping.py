from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

START_URL="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

browser = webdriver.Chrome("D:/Setup/chromedriver_win32/chromedriver.exe")
browser.get(START_URL)

soup = BeautifulSoup(browser.page_source, "html.parser")

star_table=soup.find('table')

temp_list=[]

table_rows=star_table.find_all('tr')

for tr in table_rows: 
    td = tr.find_all('td') 
    row = [i.text.rstrip() 
    for i in td]
    temp_list.append(row)

star_name=[]
star_distance=[]
star_radius=[]
star_mass=[]

for i in range(1,len(temp_list)):
    star_name.append(temp_list[i][1])
    star_distance.append(temp_list[i][3])
    star_mass.append(temp_list[i][5])
    star_radius.append(temp_list[i][6])
    df2 = pd.DataFrame(list(zip(star_name,star_distance,star_mass,star_radius)),
    columns=['Star_name','Distance','Mass','Radius'])
    df2.to_csv('Bright_star.csv')
