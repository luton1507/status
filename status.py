# -*- coding: utf-8 -*-
#trình code bạn yếu vl lulzk1d =))
import time
import sys
import os
if sys.platform == "linux" or sys.platform == "linux2":
    os.system("clear")
elif sys.platform == "win32":
    os.system("cls")
elif sys.platform == "darwin":
    os.system("clear")
else:
    print("Unknown System Detected")
try: 
 import cfscrape
except:
 print("You need install: cfscrape")
 sys.exit()
try:
 import requests
except:
 print("You need install: requests")
 sys.exit() 
print """

  /$$$$$$   /$$                 /$$                        
 /$$__  $$ | $$                | $$                        
| $$  \__//$$$$$$    /$$$$$$  /$$$$$$   /$$   /$$  /$$$$$$$
|  $$$$$$|_  $$_/   |____  $$|_  $$_/  | $$  | $$ /$$_____/
 \____  $$ | $$      /$$$$$$$  | $$    | $$  | $$|  $$$$$$ 
 /$$  \ $$ | $$ /$$ /$$__  $$  | $$ /$$| $$  | $$ \____  $$
|  $$$$$$/ |  $$$$/|  $$$$$$$  |  $$$$/|  $$$$$$/ /$$$$$$$/
 \______/   \___/   \_______/   \___/   \______/ |_______/ 
                                                                                                
      ./Checking HTTP-Status CODE Bypass Cloudflare UAM
      ./Coder by lulzk1d
      ./Github.com/lulzk1d
"""
u = raw_input("[*] Target [URL]: ")
#get status code normal
r = requests.get(u)
code = r.status_code
print ("Checking HTTP Status Code Normal: ")
time.sleep(5)
print ("[~] Sending HTTP-Request to "+u+" => "+"["+str(code)+"]")
#get status code bypass cloudflare
print("===============================================")
time.sleep(2)
print ("[+] Checking HTTP Status Code Bypass Cloudflare: ")
scraper = cfscrape.create_scraper()
while true:
    code = scraper.get(u).status_code
    print ("[+] Sending HTTP-Request to "+u+" => "+"["+str(code)+"]")

