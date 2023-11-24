import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)

FORM_NAME_FIELD = ("xpath", "//input[@id='RESULT_TextField-0']")
COPY_TEXT_LOCATOR = ("xpath", "//button[text()='Copy Text']")

driver.get("https://testautomationpractice.blogspot.com/")
driver.switch_to.frame("frame-one796456169")
time.sleep(2)

driver.find_element(*FORM_NAME_FIELD).send_keys("Anastasiia")
time.sleep(2)

driver.switch_to.default_content()
driver.find_element(*COPY_TEXT_LOCATOR).click()