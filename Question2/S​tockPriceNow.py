#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 15:42:58 2021

@author: leongkaon
@Q​uestion2: 如何爬蟲取得當刻股價
@IDE: S​pyder
"""

#%%
import requests
from bs4 import BeautifulSoup as bs

#%%
stock_number = '0001'

# get web page info
url = 'https://hk.finance.yahoo.com/quote/' + stock_number + '.HK'
response = requests.get(url)
html = bs(response.text, 'lxml')

# Find CSS
# 當前股價
price = html.find('span', class_ = 'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)').text
print(price)

# 變動值(%)
change = html.find('span', class_ = 'Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($negativeColor)').text
print(change)


# =============================================================================
# Reference:
#    https://medium.com/analytics-vidhya/how-to-get-stock-prices-in-real-time-using-python-2021-bf50c1d2378b
# =============================================================================
# 後記:
# IDE轉用Spyder感覺順手d
# 撞板撞左成個下晝,試XPATH試其他套件試其他網站
# 牛牛B​lock左HTML R​esponse 403, AAStock唔知點解搵唔到個數字
# 下次整股市特定升跌幅度時候出個A​lert比自己,經IFTTT串LINE,每十分鐘Run一次Script
# 如果再整複雜小小, 可以G​oogle Cloud開部Linux, crontab睇時間run, 咁就唔洗用屋企電腦, 而且可以確保佢run緊, 但唔知幾錢
# =============================================================================

#%% 
# =============================================================================
# Failure, XPATH時得時唔得,唔知做錯d乜,之後再試
# from lxml import etree
# url = 'https://hk.finance.yahoo.com/quote/0001.HK?p=0001.HK&.tsrc=fin-srch'
# response = requests.get(url)
# html = bs(response.text, 'html.parser')
# dom = etree.HTML(str(html))
# print(dom.xpath('//*[@id="quote-header-info"]/div[3]/div[1]/div/span[1]')[0].text)
# =============================================================================








