import re

import requests
from bs4 import BeautifulSoup
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
# r = requests.request('GET','https://book.douban.com/subject/1084336/comments/',headers=headers)
# print(r,r.text)
markup = '<p class="title"><b>A Little Prince</b></p>'
soup = BeautifulSoup(markup,"lxml")
print(soup.b)
print(type(soup.b))
print(soup.p.attrs,soup.p['class'])
print(type(soup.b.string))
print(soup.find_all('b'))
r = requests.request('GET','https://book.douban.com/subject/1084336/comments/',headers=headers)
soup1 = BeautifulSoup(r.text,"lxml")
pattern = soup1.find_all('span','short')
for item in pattern:
    print(item.string)
pattern_s = re.compile('<span class="user-stars allstar(.*?)rating"')
# p返回的是一个列表
p = re.findall(pattern_s,r.text)
s = 0
for star in p:
    s += int(star)
print(s)


