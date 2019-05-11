import requests
from bs4 import BeautifulSoup

req = requests.get('https://www.daum.net/')
soup=BeautifulSoup(req.text,'html.parser') 
s=soup.select(" ol.list_hotissue > li > div")[1].select("span")[1]

a=1
for i in s.findAll('span'):
    print(i.text)
    a=a+1


    