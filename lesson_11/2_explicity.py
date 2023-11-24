import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 15, poll_frequency=1)

#driver.get("https://demoqa.com/dynamic-properties")

#VISIBLE_AFTER_BUTTON = ("xpath", "//button[@id='visibleAfter']")
#ENABLE_IN_SECONDS = ("xpath", "//button[@id='enableAfter']")

#BUTTON = wait.until(EC.visibility_of_element_located(VISIBLE_AFTER_BUTTON))
#BUTTON.click()

#BUTTON2 = wait.until(EC.element_to_be_clickable(ENABLE_IN_SECONDS))
#BUTTON2.click()
#time.sleep(2)

driver.get("https://the-internet.herokuapp.com/dynamic_controls")

REMOVE_BUTTON = ("xpath", "//button[text()='Remove']")
driver.find_element(*REMOVE_BUTTON).click()

wait.until(EC.invisibility_of_element_located(REMOVE_BUTTON))

ENABLE_BUTTON = ("xpath", "//button[text()='Enable']")
INPUT = ("xpath","//input")
wait.until(EC.element_to_be_clickable(ENABLE_BUTTON)).click()

wait.until(EC.element_to_be_clickable(INPUT)).send_keys("Hello")
wait.until(EC.text_to_be_present_in_element_value(INPUT, "Hello"))

print ("It`s OK")
