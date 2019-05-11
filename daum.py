import requests
from bs4 import BeautifulSoup

req = requests.get('https://www.daum.net/')
soup=BeautifulSoup(req.text,'html.parser') 
a=1
s=soup.select('.hotissue_mini a[class*=link_issue]')
for i in s:
    print(a,"위",i.text)
    a=a+1
    
    #mArticle > div.cmain_tmp > div.section_media > div.hot_issue.issue_mini > div.hotissue_layer > ol > li:nth-child(3) > div > div:nth-child(1) > span.txt_issue > a
    #mArticle > div.cmain_tmp > div.section_media > div.hotissue_builtin > div.realtime_part > ol > li:nth-child(1) > div > div:nth-child(1) > span.txt_issue > a
    #mArticle > div.cmain_tmp > div.section_media > div.hot_issue.issue_mini > div.hotissue_layer > ol > li:nth-child(3) > div > div:nth-child(1) > span.txt_issue > a
    #mArticle > div.cmain_tmp > div.section_media > div.hot_issue.issue_mini.hide > div.hotissue_layer > ol > li:nth-child(3) > div > div:nth-child(1) > span.txt_issue > a