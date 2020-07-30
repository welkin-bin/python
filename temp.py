# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
"""幸运数字猜猜猜 2.0  于文斌  2020年5月30日"""
import random
random.randint(0,9)
n=1
while n<4:
 number= input("请您猜0-9中一个数字")
 guess=int(number)
 if n==3:
  if guess==random.randint(0,9):
     print("恭喜您，GOODLUCK!")
     print("您和python太有缘分了，lets go on！")
     break
  else:
      print("对不起次数已经用尽")
      break
 if guess==random.randint(0,9):
     print("恭喜您，GOODLUCK!")
     print("您和python太有缘分了，lets go on！")
     break
 else:
       if guess>random.randint(0,9):
          print("抱歉您猜大了，请再猜一次")
       else:
          print("抱歉您猜小了，请再猜一次")
 n=n+1
print("GAME OVER")
