import yfinance as yf

stock_no = '0001.hk'
start_date = '2000-01-04'
end_date = '2021-04-02'
tmp = yf.download(stock_no, start=start_date, end=end_date)
data = tmp.reset_index()
print(data.head())
print(data.tail())
#-------------------------------------------------------------------
# Source: weikaiwei.com/finance/stocker/

