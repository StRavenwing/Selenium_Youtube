import time
import os
import pathlib
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": os.path.join(pathlib.Path(__file__).parent.resolve(), 'downloads')
}
chrome_options.add_experimental_option("prefs", prefs)
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://the-internet.herokuapp.com/download")

driver.find_element("xpath", "//a[15]").click()

time.sleep(3)