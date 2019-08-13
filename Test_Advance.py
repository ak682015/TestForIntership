# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 00:01:22 2019

@author: Arman
"""
from bs4 import BeautifulSoup
import requests
import csv


name_list = []
logo_list = []
gst_list = []
add_list = []
tel_list = []
fax_list = []
mail_list = []
web_list = []
con_list = []
pro_list = []
sp_pro_list = []


def csv_entry():
    csv = open('Assignment_1.2.csv', "w+", encoding="utf-8") 
    columnTitleRow = "Name, Logo URL, Gst number, Address, Telephone, Fax, E-mail, Website, Contact, Product, Special Product\n"
    csv.write(columnTitleRow)
    #designation,linkedin,twitter,wikipedia,facebook, website = "None","None","None","None","None","None"
    for i in range(len(name_list)):
        name = name_list[i].replace('\n', "").replace(',','_')
        logo = logo_list[i].replace('\n', "").replace(',','_')
        gst = gst_list[i].replace('\n', "").replace(',','_')
        add = add_list[i].replace('\n', "").replace(',','_')
        tel = tel_list[i].replace('\n', "").replace(',','_')
        fax = fax_list[i].replace('\n', "").replace(',','_')
        mail = mail_list[i].replace('\n', "").replace(',','_')
        web = web_list[i].replace('\n', "").replace(',','_')
        con = con_list[i].replace('\n', "").replace(',','_')
        pro = pro_list[i].replace('\n', "").replace(',','_')
        sp_pro = sp_pro_list[i].replace('\n', "").replace(',','_')
        
        row = str(name) + "," + str(logo) + "," +  str(gst) + "," + str(add) + "," + str(tel) + "," + str(fax) + "," + str(mail) + "," + str(web) + "," + str(con) + "," + str(pro) + "," + str(sp_pro) + "," +"\n"
        csv.write(row)
    csv.close()

def extract_from_individual(url):
    
    page = requests.get(url)
    page_soup = BeautifulSoup(page.text,'lxml')
    
    
    try:
        name = page_soup.find('h1').text
        name_list.append(name)
    except:
        name_list.append('None')

    
    try:
        logo = page_soup.find('img',{'class':'alignnone'})['src']
        logo_list.append(logo)
    except:
        logo_list.append("None")
        
        
    try:
        #gst = page_soup.findAll('td')
        gst = page_soup.find(string="GST Registration No.:").find_next('td').text
        gst_list.append(gst)
            
    except:
        gst_list.append("None")
        
        
    try:
        #gst = page_soup.findAll('td')
        add = page_soup.find(string="Office Address:").find_next('td').text
        add_list.append(add)
        #print(add)
            
    except:
        add_list.append("None")
        
        
    try:
        #gst = page_soup.findAll('td')
        tel = page_soup.find(string="Tel:").find_next('td').text
        tel_list.append(tel)
        #print(tel)
            
    except:
        tel_list.append("None")
        
    try:
        #gst = page_soup.findAll('td')
        fax = page_soup.find(string="Fax:").find_next('td').text
        fax_list.append(fax)
        #print(fax)
            
    except:
        fax_list.append("None")
        
        
    try:
        #gst = page_soup.findAll('td')
        mail = page_soup.find(string="E-mail:").find_next('td').text
        mail_list.append(mail)
        #print(mail)
            
    except:
        mail_list.append("None")


        
    try:
        #gst = page_soup.findAll('td')
        web = page_soup.find(string="Website:").find_next('td').text
        web_list.append(web)
        #print(web)
            
    except:
        web_list.append("None")



        
    try:
        #gst = page_soup.findAll('td')
        con = page_soup.find(string="Contact & Position:").find_next('td').text
        con_list.append(con)
       # print(con)
            
    except:
        con_list.append("None")


        
    try:
        #gst = page_soup.findAll('td')
        pro = page_soup.find(string="Products:").find_next('td').text
        pro_list.append(pro)
       # print(con)
            
    except:
        pro_list.append("None")


    try:
        #gst = page_soup.findAll('td')
        sp_pro = page_soup.find(string="Special Product:").find_next('td').text
        sp_pro_list.append(sp_pro)
        print(con)
            
    except:
        sp_pro_list.append("None")

    return


def extract_link(page_soup):
    
    all_link= []
    next_link = page_soup.findAll('div',{'class':'letter-section'})

    for n in next_link:
        b = n.findAll('a')
        
        for a in b:
            all_link.append(a['href'])
    return all_link


def main():
    link = r"http://www.margma.com.my/ordinary-members/"
    page = requests.get(link)
    current_page_soup = BeautifulSoup(page.text, 'lxml')
    next_page = extract_link(current_page_soup)

    final_list = []
    for n in next_page:
        extract_from_individual(n)
        
    
    csv_entry()
      
        
   # print(final_list)
"""
	all_pages_link = []
	for i in range(0,20):
		next_page = extract_next_link(current_page_soup)
		next_page = "https://www.orate.me"+next_page

		extract_from_individual(next_page)

		all_pages_link.append(next_page)
		page = requests.get(next_page)
		current_page_soup = BeautifulSoup(page.text, 'lxml')
	
	print(all_pages_link)

	# for p in all_pages_link:
	# 	print(p)
		#extract_from_individual(p)
		# page = requests.get(next_page)
		# current_page_soup = BeautifulSoup(page.text, 'lxml')
"""


main()