from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup

def get_font_awesome_icons():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://fontawesome.com/search?p=1&o=r&m=free&s=solid")
    page_elements = driver.find_elements(By.XPATH, '/html/body/div[1]/div/main/div/div/div/div/div[2]/div[5]/div[2]/div[2]')
    
    page = 1

    icons = []
    for page_element in page_elements:
        page = page_element.get_attribute("innerHTML")
        page = ''.join(filter(str.isdigit, page.strip()))
        print('max pages', page)

    max_pages = int(page) + 1

    for i in range(1, max_pages):
        print(f'Processing page {i}')
        driver.get("https://fontawesome.com/search?p=" + str(i) + "&o=r&m=free&s=solid")

        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//span[@class="icon-name"]')))

        icon_elements = driver.find_elements(By.XPATH, '//span[@class="icon-name"]')
        for icon in icon_elements:
            icons.append(icon.text.split('\n')[0])

    driver.quit()

    return icons

icons = get_font_awesome_icons()
with open('icons.txt', 'w') as f:
    for icon in icons:
        print(icon)
        f.write(icon + '\n')