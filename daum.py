import requests
from bs4 import BeautifulSoup

req = requests.get('https://www.daum.net/')
soup=BeautifulSoup(req.text,'html.parser') 
a=1
s=soup.select('.hotissue_mini a[class*=link_issue]')
for i in s:
    print(a,"위",i.text)
    a=a+1
    
    