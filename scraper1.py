from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd
import csv

# NASA Exoplanet URL
START_URL = "https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"

# Webdriver
browser = webdriver.Chrome("E:\WEB SCRAPER\C141-Reference-code--main\chromedriver.exe")
browser.get(START_URL)
time.sleep(10)

def scrape():
    headers=["name","light_years_from_earth","planet_mass","stellar_magnitude","discovery_date"]
    planets_data=[]
    for i in range(0,20):
        #print(f'Scrapping page {i+1} ...' )
        
        # BeautifulSoup Object     
        soup = BeautifulSoup(browser.page_source, "html.parser")

        # Loop to find element using XPATH
        for ul_tag in soup.find_all("ul", attrs={"class", "exoplanet"}):

            li_tags = ul_tag.find_all("li")
           
            temp_list = []

            for index, li_tag in enumerate(li_tags):

                if index == 0:                   
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")

            planets_data.append(temp_list)
        browser.find_element(by=By.XPATH, value='//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()

    with open("scrapper_4.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(planets_data)
scrape()
