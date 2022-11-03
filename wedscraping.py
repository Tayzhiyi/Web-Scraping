from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd
import numpy as np
import csv
def write_csv(data):
    with open(r'C:\Users\tayzh\Desktop\results.csv', 'a', newline = '') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(data)

driver = webdriver.Chrome(executable_path = r"C:\Users\tayzh\Downloads\chromedriver_win32\chromedriver.exe")
baseURL = "https://www.ccilindia.com/FPI_ARCV.aspx"
time.sleep(0.2)
driver.get(baseURL)
time.sleep(0.2)
#Iterates through all the dates
for i in range(2, len(driver.find_elements("xpath", '//*[@id="drpArchival"]/option'))):
    #Iterates through the subpages on the table
    for j in range(1,len(driver.find_elements("xpath", '//*[@id="grdFPISWH"]/tbody/tr[17]/td/a')) + 1):
        time.sleep(1)
       
        #Iterates down the table
        for k in range(2, len(driver.find_elements("xpath", '//*[@id="grdFPISWH"]/tbody/tr'))):
            row = []
            
            #Iterates across each row
            for l in range(1, len(driver.find_elements("xpath", '//*[@id="grdFPISWH"]/tbody/tr[2]/td')) + 1):
                row.append(driver.find_element("xpath", f'//*[@id="grdFPISWH"]/tbody/tr[{k}]/td[{l}]').text)
                
            #adds the row to the dataframe 
            #data.loc[len(data)] = row
            write_csv(row)
            
            
        driver.find_element("xpath", f'//*[@id="grdFPISWH"]/tbody/tr[17]/td/a[{j}]').click() #Jumps from first to last page

    time.sleep(0.2)
    #Opens the date dropdown
    driver.find_element("xpath", '//*[@id="drpArchival"]').click()
    time.sleep(0.2)
    #Clicks to the next date
    driver.find_element("xpath", f'//*[@id="drpArchival"]/option[{i}]').click()

driver.quit()
