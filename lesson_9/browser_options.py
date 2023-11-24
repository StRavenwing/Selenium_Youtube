import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
chrome_options.page_load_strategy = "eager" #load DOM
chrome_options.page_load_strategy = "normal" #load full page
#chrome_options.add_argument("--haedless")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--disable-cache")
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://whatismyipaddress.com/")