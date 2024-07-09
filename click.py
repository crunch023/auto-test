from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#PATH = "/Users/admin/Downloads/chromedriver-mac-arm64/chromedriver"
url = webdriver.Chrome()
url.get("https://www.techwithtim.net")

step1python = url.find_element(By.LINK_TEXT, "Python")
step1python.click()


#whole page
main = WebDriverWait(url, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "tutorials__TutorialsList-sc-179hc97-2"))
)

#click donate button
donate = url.find_element(By.LINK_TEXT, "Donate")
donate.click()


#click patreon
main = WebDriverWait(url, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "support-donate__FlexContainer-sc-mzo9ma-1"))
)
donate = url.find_element(By.CLASS_NAME, "donate__DonateCardContainer-sc-1a8062w-0")
donate.click()

time.sleep(5)

