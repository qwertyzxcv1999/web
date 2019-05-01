from bs4 import BeautifulSoup

import requests

# web_url에 원하는 웹의 URL을 넣어주시면 됩니다.
r = requests.get(https://www.naver.com/)
r.status_code
200
r.headers['content-type']
'text/html; charset=UTF-8'
r.encoding
'UTF-8'
r.text
<!DOCTYPE html>
<html class="client-nojs" lang="en" dir="ltr">
