import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)

driver.get("https://demoqa.com/nestedframes")
driver.switch_to.frame("frame1")

print (driver.find_element("xpath","//body").text)

driver.switch_to.frame(0)
print (driver.find_element("xpath","//body").text)

driver.switch_to.parent_frame()
print (driver.find_element("xpath","//body").text)
