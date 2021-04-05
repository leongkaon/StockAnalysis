# 同另一份Python寫的一樣，呢個係R版本
# -------------------------------------------------------------------------------------------------
# Step1: 找出股價
library(quantmod);

# 港交所2000年6月27日上市
setSymbolLookup(WK=list(name='0388.hk',src="yahoo", from = as.Date("2000-06-27"), to = as.Date("2021-04-02")));
getSymbols("WK");
hk = na.omit(
        data.frame(WK)
)
dim(hk) #row: 5132
head(hk)
tail(hk)
colnames(hk)
colnames(hk) = c('Open','High','Low','Close','Volume','Adjusted')
# -----------------------------------------------------------------------------------------------
# Step2: 判斷升跌次數
rises_or_falls = hk$Close[-1] - hk$Close[1:(dim(hk)[1]-1)]

sum(rises_or_falls>0) #2414
sum(rises_or_falls<0) #2434
sum(rises_or_falls==0) #283



