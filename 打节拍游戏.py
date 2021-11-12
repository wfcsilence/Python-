import sys
import msvcrt
import time
import random

count = 0
times = [0.4,0.6,0.8,1.0]
Numbers = [4,5,6,7,8]

print('按下Y开始，按D打节拍，按其他退出游戏')
if ord(msvcrt.getch()) in [89, 121]:
  print("马上开始")
else:
  sys.exit()

while True:
  inter=random.choice(times)
  number=random.choice(Numbers)
  #print(inter,number)

  for x in range(number,1,-1):
    print(x)
    if(x>2):
      time.sleep(inter)
    else:
      starttime = time.time()
      break

  if ord(msvcrt.getch()) in [68, 100]:
    endtime = time.time()
    diff=endtime-starttime
    print(1)
    print(diff-inter)
    
    if(abs(diff-inter)<0.2):
      print("Good!")
      count+=1
      print("当前得分："+str(count))
    else:
      print("Bad!")
      print("最终得分："+str(count))
      count = 0
      print("继续？Y?")
      if ord(msvcrt.getch()) in [89, 121]:
        print("马上开始")
      else:
        sys.exit()






