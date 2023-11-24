import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from  selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 5, poll_frequency=1)

driver.get("https://the-internet.herokuapp.com/dropdown")

LOCATOR_SELECT = ("xpath", "//select[@id='dropdown']")

DROPDOWN = Select(driver.find_element(*LOCATOR_SELECT))
time.sleep(2)
#DROPDOWN.select_by_visible_text("Option 1") #choose by text
#DROPDOWN.select_by_value("2") #choose by value
#DROPDOWN.select_by_index(1) #choose by index

all_options = DROPDOWN.options

#for option in all_options:
#    time.sleep(1)
#    if "Option 1" in option.text: #check presened option
#        print ("Option is presented")
#    DROPDOWN.select_by_visible_text(option.text) #circle by text 

#for option in all_options:
#   time.sleep(1)
#   DROPDOWN.select_by_index(all_options.index(option)) #circle by index 

for option in all_options:
    time.sleep(1)
    DROPDOWN.select_by_value(option.get_attribute("value")) #circle by value