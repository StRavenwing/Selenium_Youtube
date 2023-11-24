import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)

FOR_BUSINESS_BUTTON_LOCATOR = ("xpath", "//a[text()=' For Business ']")
START_FREE_BUTTON_LOCATOR = ("xpath", "//*[@id='rec526797046']/div/div/div[5]/a") 

driver.get("https://hyperskill.org/tracks")
time.sleep(2)
print (driver.current_window_handle) #print descriptor of current window

driver.find_element(*FOR_BUSINESS_BUTTON_LOCATOR).click()
time.sleep(2)

print (driver.window_handles) #print descriptions of all opened windows

tabs = (driver.window_handles)

driver.switch_to.window(tabs[1]) 
print (driver.current_window_handle) #print decription of new current page

driver.find_element(*START_FREE_BUTTON_LOCATOR).click()
time.sleep(2)
