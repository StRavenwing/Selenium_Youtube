import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

PROXY_SERVER = "37.19.220.168:8443" #proxy in format "ip address:port"

options = Options()
options.add_argument(f"--proxy-server={PROXY_SERVER}")
driver = webdriver.Chrome(options=options)

driver.get("https://ipaddress.my/") #IP адрес: 77.137.65.219

time.sleep(5)