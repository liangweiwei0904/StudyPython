# -*- coding: utf-8 -*-
"""
Get dji stock data
@author: Dazhuang
"""
import requests
import re
def retrieve_dji_list():
    r = requests.get('https://money.cnn.com/data/markets/nasdaq/')
    print(r.status_code)
    print(r.text)
    # 先获取表头信息
    head = re.findall('<span title="Apple" class="column stock-name">(.*?)</span>', r.text)
    print(head)
    # assert len(head)==1
    table_head = ['Company'] + re.findall('<th>(.+?)<', head[0])
    # 先获取表的总体
    tbody_pat = re.compile('tbody>(.*?)</tbody')
    tbody = re.findall(tbody_pat, r.text)
    # assert len(tbody) == 1
    # 再获取总体表中每一条记录
    tr_pat = re.compile('<tr>(.*?)</tr>')
    tr_list = re.findall(tr_pat, tbody[0])
    # 最后获取每一条记录中的各个字段
    table_pat = re.compile('>([^<^&]+?)<')
    stock_list = [table_head]
    for i in tr_list:
        s = re.findall(table_pat, i)
        stock_list.append(s)
    return stock_list
dji_list = retrieve_dji_list()
print(dji_list)