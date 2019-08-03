
# -*- coding: utf-8 -*-
# :D
import sys,os,random,threading,urllib3
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
       
	./Checking HTTP-Status Code BYPASS Cloudflare UAM
	./Author: lulzkid
	./Github.com/lulzkid
"""
print("================================================")
u = raw_input("[*] Target [URL]: ")
s2 = cfscrape.create_scraper()
code3 = s2.get(u).status_code
if s2.get(u).status_code == 200:
    print "[!] HTTP " + str(code3) + " [OK]"
elif s2.get(u).status_code == 404:
    print "[!] HTTP " + str(code3) + " [Not Found]"
else:
    print "[!] HTTP " + str(code3) + " [Error or Down]"
print("================================================")
print("[*] 1. Normal")
print("[*] 2. Bypass" + " (only work on cloudflare uam)")
mode = raw_input("[*] Select Mode: ")
print("================================================")
if mode == '1':
	print("- [1] Checking HTTP Status Code Normal:")
	while True:
            try:
                i = random.choice(("[!]", "[@]", "[~]", "[+]", "[-]"))
                r = requests.get(u)
                code = r.status_code
                print i,"Sending HTTP-Requests to " + "[" + u + "]" + " => " + "Status: ["+str(code)+"]"
            except KeyboardInterrupt:
                print('./Exiting, Have fun day ;)')
                sys.exit(0)  
            except requests.exceptions.ConnectionError as e:
                print("[!]"+" Please Check Your Internet Connection!")
                sys.exit(1)  
elif mode == '2':
    print("+ [2] Checking HTTP Status Code Bypass Cloudflare UAM:") 
    while True:
        try:
            i = random.choice(("[!]", "[@]", "[~]", "[+]", "[-]"))
            s = cfscrape.create_scraper()
            code2 = s.get(u).status_code
            print i,"Sending HTTP-Requests to " + "[" + u + "]" + " => " + "Status: ["+str(code2)+"]"
        except KeyboardInterrupt:
            print('./Exiting, Have fun day ;)')
            sys.exit(0)
        except requests.exceptions.ConnectionError as e:
            print("[!]"+" Please Check Your Internet Connection!")
            sys.exit(1) 
else:
  sys.exit(0)
