from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument("--disable-notifications")

driver = webdriver.Chrome(options=options)
driver.get('https://www.facebook.com/')
driver.find_element_by_name('email').send_keys('아이디')
time.sleep(5)
driver.find_element_by_name('pass').send_keys('비밀번호')
time.sleep(5)
driver.find_element_by_id('loginbutton').click()

el = driver.find_element_by_name('xhpc_message')
contents = '셀레니움 페이스북 자동 글쓰기 테스트'
el.send_keys(contents)
time.sleep(5)
driver.find_element_by_css_selector('div._6c0p._69yt > div > div > button').click()
time.sleep(3)
driver.find_element_by_css_selector('div._6c0p._69yt > div > div > button').click()
time.sleep(3)
driver.quit()