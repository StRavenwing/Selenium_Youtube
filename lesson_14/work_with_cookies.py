import time
import os
import pickle
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10, poll_frequency=1)

driver.get("https://www.freeconferencecall.com/ru/il/login")

#LOGIN_FIELD = ("xpath", "//input[@id='login_email']")
#PASSWORD_FIELD = ("xpath", "//input[@id='password']")
#BUTTON = ("xpath", "//button[@id='loginformsubmit']")      

#driver.find_element(*LOGIN_FIELD).send_keys("lipatova_2013@inbox.ru")
#driver.find_element(*PASSWORD_FIELD).send_keys("freeconferencecall15011984")
#driver.find_element(*BUTTON).click()

#pickle.dump(driver.get_cookies(), open(os.getcwd()+"\lesson_14\cookies\cookie.pkl", "wb")) authorization and saving cookies in file

driver.delete_all_cookies() #delete all cookies

cookies = pickle.load(open(os.getcwd()+"\lesson_14\cookies\cookie.pkl", "rb")) #loading cookies fron saved file
for cookie in cookies:
    driver.add_cookie(cookie) #add new cookies
time.sleep(3)
driver.refresh()
time.sleep(3)