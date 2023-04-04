import time
import json
import sys
import os
os.system("bash tlocation.sh")
print("ctrl + c exit")
print("tron on your smartphone ")
number = int(input("enter your send sms number :-"))
time = int(input("enter sleep time :- "))
while True:
     try:
         jdata = os.popen("termux-location").read()    
         jd = json.loads(jdata)
         os.system(f"termux-sms-send -n {number} {jd} ")
         time.sleep(time)
     except:
         print("tron on location")