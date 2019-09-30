#================================================================
# Standard Modules
# => math, os, sys, datetime, time, random, urllib
#================================================================


from  calcs import *        # calcs.py 중 해당 function만 function name을 참조로 memory에 할당이 된다.
# print(plus(2,3))

import calcs                # calcs.py의 모든 function은 calcs 참조로 memory에 할당이 된다.
# print(calcs.plus(3,4))

import sys, os

# print("sys.argv: ", sys.argv)
# print("sys.version\n", sys.version)
# print("sys.copyright\n", sys.copyright)
# sys.ps1 = "python>"

# print(os.name)
# os.getcwd(), os.chdir()
# os.mkdir(), os.rmdir(), os.rename()
# os.system('dir'), os.system('cls')
# os.system('python h.py')

import datetime

now = datetime.datetime.now()
# now.# year, now.month, now.day, now.hour, now.minute, now.second
print(now)
print(now.strftime('%Y-%m-%d %H:%M:%S'))
print(now.strftime('%Y{} %m{} %d{} %H{} %M{}').format(*"년월일시분"))
print(now + datetime.timedelta(weeks=1))    #day, hours, minutes, seconds
print(now.replace(year = (now.year + 1)))
print("")

import time
st = time.time_ns()
print(st)
time.sleep(2)
print("time sleep 2 seconds!!")
print(time.time_ns() - st)
print(time.timezone / 360)

import math
#print("\n\n", dir(math))

import random
print("\n\n",dir(random))
print("random.randrange from 1 to 10: ", random.randrange(1,10))
print("random.randrange from 1 to 10: ", random.randrange(1,10))
print("random.randrange from 1 to 10: ", random.randrange(1,10))

ran_chr = list("가나다라마바사아자차카타파하")
print("random choice: ", random.choice(ran_chr))
print("random choice: ", random.choice(ran_chr))
print("random choice: ", random.choice(ran_chr))

# random.random() vs random.randrange() vs random.randint()
# random.uni(a, b)      # a와 b 사이의 랜덤 실수
lst = [5, 4, 3, 2, 1]
print("random choice 3ea", random.sample(lst, k=3))
print("random choice 3ea", random.sample(lst, k=3))
print("random choice 3ea", random.sample(lst, k=3))

import ssl
import urllib import request
ctx  = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "https://google.com"
html = urllib.request.urlopen(url, context=ctx).read()

