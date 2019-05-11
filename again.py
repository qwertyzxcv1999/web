import requests
from bs4 import BeautifulSoup

req = requests.get('https://www.daum.net/')
soup=BeautifulSoup(req.text,'html.parser') 
s=soup.find_all("span",{'class':'txt_issue'})
a=1

for i in s:
    b=a//2
    if (a%2==1) or a>30 :
       pass
    else:
        print(b,"위",i.text)
    a=a+1
    
