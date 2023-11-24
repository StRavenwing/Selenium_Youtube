import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
action = ActionChains(driver)

LEFT_BUTTON_LOCATOR = ("xpath", "//button[@id='leftClick']")
DOUBLE_BUTTON_LOCATOR = ("xpath", "//button[@id='doubleClick']")
RIGHT_BUTTON_LOCATOR = ("xpath", "//button[@id='rightClick']")
COLOR_CHANGE_BUTTON_LOCATOR = ("xpath", "//button[@id='colorChangeOnHover']")

driver.get("https://testkru.com/Elements/Buttons")

left_button = driver.find_element(*LEFT_BUTTON_LOCATOR)
double_button = driver.find_element(*DOUBLE_BUTTON_LOCATOR)
right_button = driver.find_element(*RIGHT_BUTTON_LOCATOR)
color_change_button = driver.find_element(*COLOR_CHANGE_BUTTON_LOCATOR)

action.click(left_button).pause(2).double_click(double_button).pause(2).context_click(right_button).perform()
time.sleep(3)
action.move_to_element(color_change_button).perform()
time.sleep(3)
