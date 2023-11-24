import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10, poll_frequency=1)

driver.get("https://the-internet.herokuapp.com/javascript_alerts")

#BUTTON1 = driver.find_element("xpath", "//button[@onclick='jsAlert()']")
#wait.until(EC.element_to_be_clickable(BUTTON1)).click()

#BUTTON2 = driver.find_element("xpath", "//button[@onclick='jsConfirm()']")
#wait.until(EC.element_to_be_clickable(BUTTON2)).click()

BUTTON3 = driver.find_element("xpath", "//button[@onclick='jsPrompt()']")
wait.until(EC.element_to_be_clickable(BUTTON3)).click()

alert = wait.until(EC.alert_is_present())
print (alert.text)
alert.send_keys("alert")
time.sleep(5)

alert.accept()

time.sleep(3)