# import re
# import requests
# year = 2019
# def crawler(url):
#     try:
#         r = requests.get(url)
#     except requests.exceptions.RequestException as err:
#         return err
#     r.encoding = r.apparent_encoding
# # 一定要把下面这 3 行写在同一行上
#     pattern = re.compile('href="/en/vnl/%s/women/teams/.*?">(.*?)</a></figcaption>\s+</figure>\s+</td>\s+<td></td>\s+<td class=".*?">(.*?)</td>\s+<td class=".*?">(.*?)</td>\s+<td class=".*?">(.*?)</td>' % year)
#     p = re.findall(pattern, r.text)
#     return p
# # if __name__ == "__main__":
# url = 'http://www.volleyball.world/en/vnl/%s/women/resultsandranking/round1' % year
# result = crawler(url)
# print(result)

import requests,re
from bs4 import BeautifulSoup
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
r = requests.request('GET','https://en.volleyballworld.com/en/vnl/2019/women/resultsandranking/round1',headers=headers)
pattern = re.compile('href="/en/vnl/2019/women/teams/(.*?)">(.*?)</a></figcaption>\s+</figure>\s+</td>\s+<td></td>\s+<td class="text--number group--start">(.*?)</td>\s+<td class="text--number result--highlight text--highlight">(.*?)</td>\s+<td class="text--number group--end">(.*?)</td>')
print(type(pattern))
p = re.findall(pattern,r.text)
print(p)

