# -*- coding: utf-8 -*-
# :D
import sys,os,random,time
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
 print("===================================")
 print("[-] pip install cfscrape")
 print("    [+] You need install: cfscrape")
 print("===================================") 
 sys.exit()
try:
 import requests
except:
 print("===================================")
 print("[-] pip install requests")
 print("    [+] You need install: requests")
 print("===================================") 
 sys.exit() 
print """
                   .-"      "-.  
                  /            \ 
                 |    LuLZK1D   | 
                    |,  .-.  .-.  ,| 
                 | )(__/  \__)( | 
                 |/     /\     \| 
       (@_       (_     ^^     _) 
  _     ) \_______\__|IIIIII|__/__________________________ 
 (_)@8@8{}<________|-\IIIIII/-|_S_O_S_S_O_S_S_O_S_S_O_S_P_> 
        )_/        \          / 
       (@           `--------` Welcome! 
       
	./Beta Checking HTTP-Status Code v1
	./Author: lulzkid
	./Github.com/lulzkid
"""
print("================================================")
u = raw_input("[*] Target [URL]: ")
if "://" in u:
   u=u.split('://')[1]
   u=u.split('/')[0]
else:
    print("[!] Invalid URL, PLEASE Add HTTP/HTTPs on URL")
    time.sleep(3)
    sys.exit(3)
api = "http://ip-api.com/json/"
data = requests.get(api+u).json()
sys.stdout.flush()
print "[*] ISP:", data['isp']
print("================================================")
if 'Cloudflare, Inc.' in data['isp']:
    enter2 = raw_input("[] Press 'Enter' to Started: ")
    print("- [] Checking Target: "+"["+u+"]"+ "\n [] HTTP Status Bypass Cloudflare")
    u2 = 'http://' + u
    scrape = cfscrape.create_scraper()
    while True:
        try:
            i = random.choice(("[!]","[@]","[#]","[-]"))
            s2 = scrape.get(u2).status_code
            print (i + " ["+u+"]"+" => "+ "Status: "+"["+str(s2))+"]"
        except Exception as e:
            if "The read operation timed out" in str(e):
                print(i+"Server maybe Down!")
        except KeyboardInterrupt:
            print ("./Exiting.. Have fun day")
            sys.exit(0)
else:
    enter = raw_input("[] Press 'Enter' to Started: ")
    print("- [] Checking Target: "+"["+u+"]"+ "\n [] HTTP Status Normal")
    u3 = 'http://' + u
    while True:
        try:
            i = random.choice(("[!]","[@]","[#]","[-]"))
            rq = requests.get(u3).status_code
            print (i + " ["+u+"]"+" => "+ "Status: "+"["+str(rq))+"]"
        except Exception as e:
            if "The read operation timed out" in str(e):
                print(i+"Server maybe Down!")
        except KeyboardInterrupt:
            print ("./Exiting.. Have fun day")
            sys.exit(0)
