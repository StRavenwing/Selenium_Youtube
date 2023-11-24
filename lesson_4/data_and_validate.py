import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://ru.wikipedia.org/")

url = driver.current_url
print (url)
assert url == "https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0", "Открыта не та страница"

current_title = driver.title
print (current_title)
assert current_title == "Википедия — свободная энциклопедия", "Неверный тайтл"



time.sleep(3)