import tushare as ts
import sys
import time

ts.set_token('79b245472a0bff65e5b605c6b1e7fb8af0da4dd9f70c08f478a4e9c4')
pro = ts.pro_api()
print("No more than two checks per minute~")
while True:
  
  time1=input("\nPlease input date, ex:20210101\n")
  try:
    df = pro.cctv_news(date=time1)
    x=0
    for i in df.values:
      x+=1
      print(" "*2+str(x)+"."+i[1] + "\n" + " "*2+i[2] + "\n")
  except:
    print('Please wait 1 minute~\n')
    starttime=time.time()
    while round(time.time() - starttime, 0)<=60:
      if round(time.time() - starttime, 0)<=59:
        print('Count:', round(time.time() - starttime, 0), 'second', end="\r")
        time.sleep(1)
      else:
        print('Count:', round(time.time() - starttime, 0), 'second', end='\r')
        print('Count: finish~          ')
        time.sleep(1)

  choose=input("Continue? y/n\n")
  if choose=="y":
    x=0
  else:
    sys.exit(0)
