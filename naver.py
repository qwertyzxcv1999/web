import requests
from bs4 import BeautifulSoup

req = requests.get('https://www.naver.com/')
soup=BeautifulSoup(req.text,'html.parser') 
s=soup.find_all("span",{'class':'ah_k'})
a=1
for i in s:

    print(a,"위",i.text)
    a=a+1