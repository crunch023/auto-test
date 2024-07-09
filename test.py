from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#PATH = "/Users/admin/Downloads/chromedriver-mac-arm64/chromedriver"
url = webdriver.Chrome()
url.get("https://www.python.org/")


"""
#login test alphabet only
storeSearch = url.find_element(By.ID, "user-name")
storeSearch.send_keys("hello123123")

#password
storeSearch = url.find_element(By.ID, "password")
storeSearch.send_keys("hellopasword")

storeSearch.send_keys(Keys.RETURN)

"""
try:
    #first page
    main = WebDriverWait(url, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "search-the-site"))
        )
    pythonSearch = main.find_element(By.ID, "id-search-field")
    failCatcher = "test1"
    pythonSearch.send_keys("test")
    failCatcher = "test2"
    pythonSearch.send_keys(Keys.RETURN)
    failCatcher = "test3"   
except:
    print("failed to test first page")




try:
    #second page
    main = WebDriverWait(url, 5).until(
           EC.presence_of_element_located((By.CLASS_NAME, "main-content "))
        )
    failCatcher = "test4"
    pythonSearchNext = main.find_element(By.LINK_TEXT, "Next »")
    failCatcher = "test5"
    pythonSearchNext.click()
    failCatcher = "test6"
except:
    print(main.text)

if(failCatcher == "test6"):
    print("All test passed")
   
   
time.sleep(2)
print("test passed up to "+failCatcher)

    





