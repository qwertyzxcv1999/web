from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
import os
import urllib
from urllib.request import urlopen
import argparse
import requests as req
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
def main():

    # 사용한 구글 url https://www.google.co.kr/search?q=%EB%B2%A4&tbm=isch

    url_info = "https://www.google.co.kr/search?"

    #params에 딕션을 넣어줌
    params = {
        #명령행에서 받은 인자값을 people로 넣어줌
        "q" : people,
        "tbm":"isch"
    }
    #url 요청 파싱값
    html_object = req.get(url_info,params) #html_object html source 값

    if html_object.status_code == 200:
        #페이지 status_code 가 200 일때 2XX 는 성공을 이야기함
        bs_object = BeautifulSoup(html_object.text,"html.parser")
        #인스턴스 생성
        img_data = bs_object.find_all("img")
        #인스턴스의 find_all 이라는 함수에 img 태그가 있으면 img_data에 넣어줌

        for i in enumerate(img_data[1:]):
            #딕셔너리를 순서대로 넣어줌
            t = urlopen(i[1].attrs['src']).read()


            filename = "byeongwoo_"+str(i[0]+1)+'.jpg'


            with open(filename,"wb") as f:


                f.write(t)
            print("Img Save Success")



#찾고자 하는 검색어를 url로 만들어 준다.
searchterm = input()
url = "https://www.google.com/search?q="+searchterm+"&source=lnms&tbm=isch"
# chrom webdriver 사용하여 브라우저를 가져온다.
browser = webdriver.Chrome()
browser.get(url)
# User-Agent를 통해 봇이 아닌 유저정보라는 것을 위해 사용
header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
# 이미지 카운트 (이미지 저장할 때 사용하기 위해서)
counter = 0
succounter = 0

 
print(os.path)
# 소스코드가 있는 경로에 '검색어' 폴더가 없으면 만들어준다.(이미지 저장 폴더를 위해서) 
if not os.path.exists(searchterm):
    os.mkdir(searchterm)
 
for _ in range(500):
    # 가로 = 0, 세로 = 10000 픽셀 스크롤한다.
    browser.execute_script("window.scrollBy(0,10000)")
for x in browser.find_elements_by_xpath('//div[contains(@class,"rg_meta")]'):
    counter = counter + 1
    print ("Total Count:", counter)
    print ("Succsessful Count:", succounter)
    print ("URL:",json.loads(x.get_attribute('innerHTML'))["ou"])
 
    # 이미지 url
    img = json.loads(x.get_attribute('innerHTML'))["ou"]
    # 이미지 확장자
    imgtype = json.loads(x.get_attribute('innerHTML'))["ity"]
    
    # 구글 이미지를 읽고 저장한다.
    try:
       if __name__=="__main__":
            main()
    except:
            print ("can't get img")
            
print (succounter, "succesfully downloaded")
browser.close() 