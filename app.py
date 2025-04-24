import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# from requests_html import HTMLSession
# from requests_html import ht
# from requests_html import AsyncHTMLSession
# from lxml_html_clean import clean_html

options = Options()
options.add_argument("--headless")  # Run browser in headless mode
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")


url = "https://uwflow.com/course/psych101"

driver = webdriver.Chrome(options=options)
driver.get(url)

element = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "div.sc-qXRQq.jtOWzV")))

for e in element:
    print(e.text)
# print(element)
# for i in element:
#     print("bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")
#     print(i.text)

driver.quit()

# session = HTMLSession()
# r = session.get(url)

# r.HTML.
# chrome_options = webdriver.ChromeOptions()

# service = Service(executable_path="chromedriver.exe")
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)


# driver.get(url)

# wait = WebDriverWait(driver, 30)

# test = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "sc-qXRQq jtOWzV")))
# soup = BeautifulSoup(test.get)





# page = requests.get(url)

# time.sleep(10)
# soup = BeautifulSoup(page.content, 'html.parser')

# print(soup.prettify())

# cards = soup.find_all('div', id='root')

# print(cards)