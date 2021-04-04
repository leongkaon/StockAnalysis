import requests
import json
import numpy as np
import pandas as pd

# yahoo hk stock url
# period1=946944000 --> 2000年1月04日
# period2=1617408000 --> 2021年4月03日
# 長和 (0001.HK)
url = "https://query1.finance.yahoo.com/v8/finance/chart/0001.hk?period1=0&period2=1549258857&interval=1d&events=history&=hP2rOschxO0"

raw = requests.get(url)

print(raw)
# HTTP 200 --> Successful responses

tmp = json.loads(raw.text)
#print(tmp)
data = pd.DataFrame(tmp['chart']['result'][0]['indicators']['quote'][0], index=pd.to_datetime(np.array(tmp['chart']['result'][0]['timestamp'])*1000*1000*1000))
print(data.head())
