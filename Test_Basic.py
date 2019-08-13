# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 23:36:57 2019

@author: Arman
"""
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import csv

url = r"http://www.veia.org.vn/default.asp?xt=xt5&page=content&linkID=34&menu=2"
page = requests.get(url)
soup = BeautifulSoup(page.text,'lxml')

frame_link = "http://www.veia.org.vn" + soup.find('iframe',{"id":"datamainX"})['src']

driver = webdriver.Chrome(executable_path=r"D:\ArmanK\chromedriver.exe")
driver.get(frame_link)

iframe = driver.find_element_by_tag_name("frame")
driver.switch_to.default_content()
driver.switch_to.frame(iframe)

new_soup = BeautifulSoup(driver.page_source,'lxml')

all_tr = new_soup.findAll('tr')

i = 1
all_td = []
sr_no_list = []
first_name_list = []
second_details_list = []
third_activity_list = []
fourth_contacts_list = [] 

for a in all_tr:
    all_td.append(a.findAll('td'))
    
    
for b in all_td:
    if len(b)>1: 
        try:
            sr_no_list.append(i)
            first_name_list.append(b[1].text)
            i += 1 
        except:
            first_name_list.append('None')
        try:
            second_details_list.append(b[2].text)
        except:
             second_details_list.append('None')     
        try:
            third_activity_list.append(b[3].text)
        except:
            third_activity_list.append('None') 
        try:
            fourth_contacts_list.append(b[4].text)
        except:
            fourth_contacts_list.append('None')
           

for i in range(len(first_name_list)):
    first_name_list[i] = first_name_list[i].replace('\xa0'," ").replace('\n',' ').replace('  ','').replace(',','_')
    second_details_list[i] = second_details_list[i].replace('\xa0'," ").replace('\n',' ').replace('  ','').replace(',','_')
    third_activity_list[i] = third_activity_list[i].replace('\xa0'," ").replace('\n',' ').replace('  ','').replace(',','_')
    fourth_contacts_list[i] = fourth_contacts_list[i].replace('\xa0'," ").replace('\n',' ').replace('  ','').replace(',','_')
        
        
        

csv = open('Assignment_1.csv', "a+", encoding="utf-8") 
columnTitleRow = "SR No,TÊN CÔNG TY,ĐỊA CHỈ	,LĨNH VỰC HOẠT ĐỘNG,EMAIL\n"
csv.write(columnTitleRow)
	
#designation,linkedin,twitter,wikipedia,facebook, website = "None","None","None","None","None","None"


for i in range(len(first_name_list)):
    zero_col = sr_no_list[i]
    first_col = first_name_list[i]
    sec_col = second_details_list[i]
    third_col = third_activity_list[i]
    fourth_col = fourth_contacts_list[i]


    row = str(zero_col) + "," + str(first_col) + "," +  str(sec_col) + "," + str(third_col) + "," + str(fourth_col)  + "\n"
    csv.write(row)

	
csv.close()


























