import urllib.request

url = "https://www.hankyung.com/feed/it.xml"

request = urllib.request.Request(url)

response = urllib.request.urlopen(request)

# print(response.read())

#xml 파싱

#메모리의 트리 형태로 펼치기
import xml.etree.ElementTree as etree

tree = etree.parse(response)

#루트 찾기
xroot = tree.getroot()

print("xroot", xroot)
print(xroot.keys())
print(xroot.items())