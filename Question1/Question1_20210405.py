# Question1
# Date: 20210405
# Version: 1.0
# Pycharm shortcut: [Alt]+[Shift]+[e] run single line
# Description:
#   早排同筆友傾計，佢提到「股市得1/4時間係升」，我地可以證實下係唔係，順手熟習Python。
#   假設以2000年至近日(2020年4月1)，以每日收盤價為基準計算，以「今日」減「上個收市日」是否大於0 判斷係升或跌
#   號碼我揀左0388.hk，應該可以代表整體香港股市?
#-------------------------------------------------------------------------------------
import numpy as np
import pandas as pd
import yfinance as yf
#-------------------------------------------------------------------------------------
# Step1: 找出股價
stock_no = '0388.hk'
# 港交所2000年6月27日上市
start_date = '2000-06-27'
# 4月2放假,所以其實係去到4月1(星期四)
end_date = '2021-04-02'
tmp = yf.download(stock_no, start=start_date, end=end_date)
data = tmp.reset_index()
print(data.head())
print(data.tail())
#-------------------------------------------------------------------------------------
# Step2: 判斷升跌次數
print(data.index) # row:5132, 總共開市日係5132日
print(data.shape[0]) # similar to print(data.index)
# 後項減前項,要轉做Array先可以加減，或者可以寫迴圈
rises_or_falls = (data['Close'][1:data.shape[0]].array - data['Close'][0:(data.shape[0]-1)].array)
print(rises_or_falls)
sum(rises_or_falls > 0) #2414日係升
sum(rises_or_falls < 0) #2434日係跌
sum(rises_or_falls == 0) #283日係無變化
#-------------------------------------------------------------------------------------
# 結論: 無考慮升跌百份比情況下，單純以「升」或「跌」判斷，港交所(0388.hk)有2414日係升，2434日係跌。升:跌大約0.99:1。