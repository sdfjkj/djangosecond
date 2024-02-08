import requests
import bs4

resp = requests.get("http://finance.daum.net/")
html = resp.text
print(html)

#html 파싱
bs = bs4.BeautifulSoup(html, 'html.parser')
#html 에서 body태그 안의 span태그의 텍스트 가져오기
print(bs.body.span.get_text())

