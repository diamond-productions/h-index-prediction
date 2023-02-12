import csv
from bs4 import BeautifulSoup as bs

# initiallize firefox webdriver 
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.window import WindowTypes
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install())) 
driver.get("https://www.researchgate.net/login")

password = driver.find_element(By.ID, "input-password")
username = driver.find_element(By.ID, "input-login")

username.send_keys("ozdi@my.hit.ac.il")
password.send_keys("xKCB5FpQevmMcLk")
password.send_keys(Keys.RETURN)

links = list()
with open('./datafiles/universities_latin_america','r') as f:
    names = f.read()
names= names.split("\n")
for name in names:
    #fill the search box and press enter
    searchbox = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="header-search-action"]')))
    searchbox.click()
    searchbox.send_keys(name , Keys.RETURN)
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[3]/div[1]/div/div/div/div/div/div[2]/div/div[2]/div/div/div/ul/li[6]/div/span'))).click
    #copy link for institution
    WebDriverWait(driver , 5)
    uni = driver.find_element(By.XPATH , '/html/body/div[1]/div[3]/div[1]/div/div/div/div/div/div[4]/div/div[2]/div/div[1]/div/div/div/div[1]/div/div[2]/div/a')
    links.append("https://www.researchgate.net"+uni.get_attribute('href'))

driver.close()
print(links)
#write links to csv 
with open('links_for_institutions' , 'w') as f:
    write = csv.write(f)
    write.writerows(links)
print("Done")



    
