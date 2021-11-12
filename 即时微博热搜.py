import requests
import sys
from lxml import etree
import time

print("你好吖(●'◡'●)")
answer=input("要开始嘛？y/n\n")
if answer=="y":
    print("OK!\n")
    time.sleep(1)
else:
    print("Bye~")
    sys.exit(0)

while True:
    url='https://s.weibo.com/top/summary?Refer=top_hot&topnav=1&wvr='
    header={'cookie':"SINAGLOBAL=7254774839451.836.1628626364688; SUB=_2AkMWR_ROf8NxqwJRmf8cymjraIt-ygDEieKgGwWVJRMxHRl-yT9jqmUgtRB6PcfaoQpx1lJ1uirGAtLgm7UgNIYfEEnw; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WWEs5v92H1qMCCxQX.d-5iG; UOR=,,www.baidu.com; _s_tentry=-; Apache=1090953026415.7019.1632559647541; ULV=1632559647546:8:4:2:1090953026415.7019.1632559647541:1632110419050; WBtopGlobal_register_version=2021092517; WBStorage=6ff1c79b|undefined",
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
    resp = requests.get (url,headers=header)
    resp1 = resp.content.decode(encoding='utf-8',errors='ignore')
    resp2=etree.HTML(resp1)
    title = resp2.xpath('//*[@id="pl_top_realtimehot"]/table/tbody/tr/td/a/text()')
    x=0
    for i in range(50):
        x=x+1
        title[i]=str(x)+"."+title[i]
    print(time.strftime("%F,%R")+'\n微博热搜\n')
    for i in range(50):
        print (''.join([title[i]]),'')
    time.sleep(1)
    answer=input("\n要继续嘛？y/n\n")
    if answer=="y":
        print("OK!\n")
        time.sleep(1)
    else:
        print("Bye~")
        time.sleep(1)
        sys.exit(0)