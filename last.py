from urllib.request import urlopen
import argparse
import requests as req
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

parser = argparse.ArgumentParser()
#argparse 모듈 에 ArgumentParse() 함수 사용하여 parser 생성


args = parser.parse_args()
#parse에 add_argument()함수 사용해 args 인스턴스생성

scroll_time=0
print("이미지 모으고 싶은것")
search_object=input("")
url_info = "https://www.google.co.kr/search?q="
url_use =url_info+search_object+("&source=lnms&tbm=isch&sa=X&ved")
url_use = str(url_use)

driver = webdriver.Chrome()
for scroll_time in range(10):

    # 사용한 구글 url https://www.google.co.kr/search?q=%EB%B2%A4&tbm=isch    
    #url 요청 파싱값
    if scroll_time < 10 :
        html_object = driver.get(url_use) #html_object html source 값
        bs_object = BeautifulSoup(html_object.text,"html.parser")
        #인스턴스 생성
        img_data = bs_object.find_all("img")
        #인스턴스의 find_all 이라는 함수에 img 태그가 있으면 img_data에 넣어줌

        for i in enumerate(img_data[1:]):
            #딕셔너리를 순서대로 넣어줌
            t = urlopen(i[1].attrs['src']).read()


            filename = str(i[0]+1)+'.jpg'


            with open(filename,"wb") as f:


                f.write(t)
            print("Img Save Success")
    scroll_time+=1
    html_object.send


