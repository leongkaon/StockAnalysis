# StockAnalysis
just for fun

-----------------------------------------------------------------

# Question1  
Date: 20210405  
Description:  
早排同筆友傾計，佢提到「股市得1/4時間係升」，我地可以證實下係唔係，順手熟習Python。  
假設以2000年至近日(2020年4月1)，以每日收盤價為基準計算，以「今日」減「上個收市日」是否大於0 判斷係升或跌  
號碼我揀左0388.hk，應該可以代表整體香港股市?  

結論: 無考慮升跌百份比情況下，單純以「升」或「跌」判斷，港交所(0388.hk)有2414日係升，2434日係跌。升:跌大約0.99:1。  

-----------------------------------------------------------------

# Question2  
Date: 20210411  
Description:  
經yahoo finance取得此刻股價。用Python　BeautifulSoup套件，加少少CSS知識。
唔難，但係唔熟，撞左成個下晝。之後會試時間，例如每十分鐘迴圈一次，然後IFTTT連LINE，當升跌幅度唔對路戈陣send message比我。

# Question2.1  
Date: 20210614  
Description:  
續上次，取得當刻股價後經IFTTT傳送至LINE。須先註冊IFTTT帳號新增Applets使用Webhooks，以POST方式傳送  
原本幾個月前係諗住Line自動報價，但而家其實好少睇，所以而家係諗住有條件通知。升或跌某個percentage或者某個價先通知我,或者出現某種走勢型態先通知  

-----------------------------------------------------------------
