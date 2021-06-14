#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 16:27:48 2021
@author: leongkaon
@Q​uestion2.1: 如何爬蟲取得當刻股價，並透過IFTTT傳至LINE
@IDE: S​pyder
"""

#%%

import requests
from bs4 import BeautifulSoup as bs

stock_number = '0005'

# get web page info
url = 'https://hk.finance.yahoo.com/quote/' + stock_number + '.HK'
response = requests.get(url)
html = bs(response.text, 'lxml')

# Find CSS

# 公司名
name = html.find('h1', class_ = 'D(ib) Fz(18px)').text
print(name)

# 當前股價
price = html.find('span', class_ = 'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)').text
print(price)

# 變動值(%)
try: 
    change = html.find('span', class_ = 'Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($negativeColor)').text
except: 
     change = html.find('span', class_ = 'Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($positiveColor)').text

print(change)


#%%
# url post
# 試過用L​inux command url post但係會miss左data, 唔知點解，所以轉用selenium直接開Browser
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get('https://maker.ifttt.com/trigger/stock_price/with/key/<YOUR KEY>' +
          'value1=' + name + '&' + 
          'value2=' + price + '&' + 
          'value3=' + change)

browser.close()

#%%

# 原本幾個月前係諗住Line自動報價，但而家其實好少睇，所以而家係諗住有條件通知。升或跌某個​percentage或者某個價先通知我,或者出現某種走勢型態先通知

























