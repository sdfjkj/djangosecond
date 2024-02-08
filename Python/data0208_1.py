import urllib.request
import xml.etree.ElementTree as et

#사용할 데이터 읽어오기
url = "https://www.hankyung.com/feed/sports"
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
# print(response.read())

#메모리에 트리 형태로 펼치기
import xml.etree.ElementTree as et
tree = et.parse(response)

#루트 찾기
xroot = tree.getroot()
print(xroot)