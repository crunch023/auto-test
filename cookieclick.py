from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as AC
import time

url = webdriver.Chrome()
url.get("https://orteil.dashnet.org/cookieclicker/")

#wait 5 seconds
url.implicitly_wait(5)

cookieCLick = url.find_element(By.ID, "bigCookie")
cookieCount = url.find_element(By.ID, "cookies")

cookieUpgrade = [url.find_element(By.ID, "productPrice0" + str(i)) for i in range(1,-1,-1)]
#grandma = url.find_element(By.ID, "productPrice1")


for i in range(1000):
    actions = AC(url)
    actions.click(cookieCLick)
    actions.perform()

time.sleep(500)