from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
print("원하는 검색어를 입력하세요")
search_object=input()
driver = webdriver.Chrome()
driver.implicitly_wait(0.3)
url="https://www.google.co.in/search?q="+search_object+"&source=lnms&tbm=isch"
driver.get(url)

for scroll in range(1000):
    driver.execute_script('window.scrollBy(0,10000)')
for idx, el in enumerate(driver.find_element_by_class_name("rg_ic")):
    driver.find_elements_by_xpath('//*[@img]')

driver.close
