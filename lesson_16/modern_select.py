import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from  selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 5, poll_frequency=1)

driver.get("https://demoqa.com/select-menu")

#LOCATOR_SELECT = ("xpath", "//input[@id='react-select-3-input']")

#driver.find_element(*LOCATOR_SELECT).send_keys("Ms.")
#time.sleep(2)
#driver.find_element(*LOCATOR_SELECT).send_keys(Keys.ENTER)   #Easy way with using keys
#time.sleep(2)

SELECT_ONE = ("xpath", "//div[@id='selectOne']") #Hard way with using slosing elements
PROF_OPTION = ("xpath", "//div[text()='Prof.']")

driver.find_element(*SELECT_ONE).click()
time.sleep(2)
driver.find_element(*PROF_OPTION).click()
time.sleep(2)