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

key = "K83572243488957"

class Course:    
    def __init__(self, code:str):
        self.code = code

    def set_easy(self, easy_ranking):
        self.easy = easy_ranking
    
    def set_liked(self, liked_ranking):
        self.liked = liked_ranking
    def set_useful(self, useful_ranking):
        self.useful = useful_ranking

class ImageParse:
    def __init__(self, file):
        self.file = file

    def api_call(self):
        
        payload = {
            'apikey': 'K83572243488957',
            'isOverlayRequired': False,
            'language': 'eng'
        }

        with open(self.file,'rb') as f:
            r = requests.post('https://api.ocr.space/parse/image',
                              files={self.file: f},
                              data=payload
                              )
            return r.content.decode()


        # myfiles = {'file': open(self.file, 'rb')}
        # r = requests.post('https://api.ocr.space/parse/image', files=myfiles)
        # print(r.text)
        

imageread = ImageParse('./sc.png')
test = imageread.api_call()
print(test)

course_list = [Course("psych101"), Course("cs137"), Course("math135"), Course("cs138"), Course("ece105")]

options = Options()
options.add_argument("--headless")  # Run browser in headless mode
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

url = f"https://uwflow.com/course/{course_list[3].code}"

driver = webdriver.Chrome(options=options)

for course in course_list:
    url = f"https://uwflow.com/course/{course.code}"

    driver.get(url)

    element = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "div.sc-qXRQq.jtOWzV")))

    course.set_easy(element[0].text)
    course.set_useful(element[1].text)




course_list.sort(key=lambda x: x.easy, reverse=True)

for c in course_list:
    print(f"code: {c.code} || easy: {c.easy} || usefullness: {c.useful}")

driver.quit()


