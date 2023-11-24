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

driver.get("https://the-internet.herokuapp.com/key_presses")

KEYBOARD_INPUT = ("id", "target")

driver.find_element(*KEYBOARD_INPUT).send_keys("hsgejflgewflgl")
time.sleep(2)

driver.find_element(*KEYBOARD_INPUT).send_keys(Keys.CONTROL+"A")
time.sleep(2)

driver.find_element(*KEYBOARD_INPUT).send_keys(Keys.BACKSPACE)
time.sleep(2)