import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)
action = ActionChains(driver)

HOVER_MENU_LOCATOR = ("xpath", "//a[text()='Main Item 2']")
HOVER_SUBMENU_LOCATOR = ("xpath", "//a[text()='SUB SUB LIST »']")
SUBMENU2_LOCATOR = ("xpath", "//a[text()='Sub Sub Item 2']")

driver.get("https://demoqa.com/menu")

hover_menu = driver.find_element(*HOVER_MENU_LOCATOR)
hover_submenu = driver.find_element(*HOVER_SUBMENU_LOCATOR)
submenu2 = driver.find_element(*SUBMENU2_LOCATOR)

action.move_to_element(hover_menu).pause(2).move_to_element(hover_submenu).click(submenu2).pause(2).perform()
time.sleep(3)