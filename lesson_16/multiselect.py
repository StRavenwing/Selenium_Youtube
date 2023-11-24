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

MULTISELECT_INPUT = ("xpath", "//input[@id='react-select-4-input']")

driver.find_element(*MULTISELECT_INPUT).send_keys("Blue")
time.sleep(2)
driver.find_element(*MULTISELECT_INPUT).send_keys(Keys.TAB)
time.sleep(2)

driver.find_element(*MULTISELECT_INPUT).send_keys("Bla")
time.sleep(2)
driver.find_element(*MULTISELECT_INPUT).send_keys(Keys.TAB)
time.sleep(2)