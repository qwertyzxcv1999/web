from selenium import webdriver
from bs4 import BeautifulSoup
import time
#기본 세팅
#크롬 구버전으로 세팅해야만 돌아감
driver = webdriver.Chrome('C:/Users/anjrm/Downloads/chromedriver')
driver.implicitly_wait(3)

browser = webdriver.Chrome()
browser.get("http://python.org")
 
menus = browser.find_elements_by_css_selector('#top ul.menu li')
 
pypi = None
for m in menus:
    if m.text == "PyPI":
        pypi = m
    print(m.text)
 
pypi.click()  # 클릭
 
time.sleep(5) # 5초 대기
browser.quit() # 브라우저 종료




# 여기부분은 네이버 들어가서 쇼핑리스트 받아오는것
# driver.get('https://nid.naver.com/nidlogin.login')
# driver.find_element_by_name('id').send_keys('anjrmfsjrjwl ')
# driver.find_element_by_name('pw').send_keys('asdasfasa')
# driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
# #캡챠있어서 막혓음 그래서 뒤에 부분도 진행이 되지 않는듯.
# driver.get('https://order.pay.naver.com/home')
# html = driver.page_source
# soup = BeautifulSoup(html, 'html.parser')
# notices = soup.select('div.p_inr > div.p_info > a > span')
#for n in notices:
#   print(n.text.strip())
