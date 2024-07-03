from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#PATH = "/Users/admin/Downloads/chromedriver-mac-arm64/chromedriver"
url = webdriver.Chrome()

#url.get("https://techwithtim.net")
url.get("https://www.techwithtim.net/tutorials")
#url.get("https://www.saucedemo.com/")

"""
#login test alphabet only
storeSearch = url.find_element(By.ID, "user-name")
storeSearch.send_keys("hello123123")

#password
storeSearch = url.find_element(By.ID, "password")
storeSearch.send_keys("hellopasword")

storeSearch.send_keys(Keys.RETURN)

"""



a=0
#varArticles = url.find_element(By.CLASS_NAME, "tutorials__TutorialsList-sc-179hc97-2 jWxNWw")

try:
    
    main = WebDriverWait(url, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "tutorials__TutorialsList-sc-179hc97-2"))
    )
    articles = main.find_elements(By.CLASS_NAME, "tutorial__TutorialCardContainer-sc-1rebzxr-0")
    for article in articles:
        header = article.find_element(By.CLASS_NAME, "tutorial__TutorialCardTitle-sc-1rebzxr-3")
        print(header.text)
    

finally:
    url.quit()
    





