import requests, json
import pandas as pd
url = 'http://21.push2.eastmoney.com/api/qt/clist/get?cb=jQuery112407201580659678162_1581950914193&pn=1&pz=20000&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:0+t:6,m:0+t:13,m:0+t:80,m:1+t:2,m:1+t:23&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152&_=1581950914194'
headers = {
    'UserAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'}
html = requests.get(url, headers=headers)
jsons = html.text[42:-2]
text_json = json.loads(jsons)
data = pd.DataFrame((text_json['data']['diff']))
columns = {
    'f2': '最新价',
    'f3': '涨跌幅%',
    'f4': '涨跌额',
    'f5': '成交量(手）',
    'f6': '成交额',
    'f7': '振幅%',
    'f8': '换手率%',
    'f9': '市盈率%',
    'f10': '量比',
    'f11': '5分钟涨跌',
    'f12': '代码',
    'f13': '所属交易所',
    'f14': '名称',
    'f15': '最高',
    'f16': '最低',
    'f17': '今开',
    'f18': '昨收',
    'f20': '总市值',
    'f21': '流通市值',
    'f22': '涨速',
    'f23': '市净率%',
    'f24': '60日涨跌幅',
    'f25': '年初至今涨跌幅',
    'f62': '主力净流入',
    'f115': '市盈率',
    'f128': '领涨股',
    'f136': '涨跌幅'
}
data = data.rename(columns=columns)
data = data.drop(['f1', 'f140', 'f141', 'f152'], axis=1)
print(data)
data.to_excel('A股股票数据.xlsx',index=False)