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

def update():
  os.system('git pull')
def clear():
  os.system('clear')
def banner():
	print('''
      	\x1b[1;93m_______           ______   _______  _                 ______  
       (  ____ )|\     /|(  __  \ (  ___  )( \      |\     /|(  __  \ 
       | (    )|| )   ( || (  \  )| (   ) || (      ( \   / )| (  \  )
       | (____)|| |   | || |   ) || (___) || | _____ \ (_) / | |   ) |
       |     __)| |   | || |   | ||  ___  || |(_____) ) _ (  | |   | |
       | (\ (   | |   | || |   ) || (   ) || |       / ( ) \ | |   ) |
       | ) \ \__| (___) || (__/  )| )   ( || (____/\( /   \ )| (__/  )
       |/   \__/(_______)(______/ |/     \|(_______/|/     \|(______/ 
       ''')
       
class login:
	update()
	clear()
	banner()
	sol='[1] MY Social media\n[2] MENU\n[3] EXIT'
	soi=nel(sol,style='green')
	cetak(nel(soi,style='cyan',title='PILIHAN MENU'))
	coi = input('\x1b[1;92m[?] pilih : ')
	if coi in ['1','01']:
		print('\x1b[1;93mKamu akan di arahkan ke link...');time.sleep(1);os.system('xdg-open https://linktr.ee/mikaz_')
	elif coi in ['2','02']:
		clear()
		banner()
		sky='[1] Doa Pemancar aura\n[2] HACK\n[3] BACK TO MENU'
		lop=nel(sky,style='green')
		cetak(nel(lop,style='cyan',title='MENU'))
		usna = input('\x1b[1;93m[?] pilih :')
		if usna in ['1']:
			oss='Iż qāla yụsufu li`abīhi yā abati innī ra`aitu aḥada asyara kaukabaw wasy-syamsa wal-qamara ra`aituhum lī sājidīn\n\nArtinya: (Ingatlah), ketika Yusuf berkata kepada ayahnya: "Wahai ayahku, sesungguhnya aku bermimpi melihat sebelas bintang, matahari dan bulan; kulihat semuanya sujud kepadaku".'
			oos=nel(oss,style='green')
			cetak(nel(oos,style='cyan',title='Surah Yusuf Ayat 4'))
		elif usna in ['2']:
		       from src import Hc
		elif usna in ['3']:
			os.system('python run.py')
		else:
			os.system('python run.py')
	elif coi in ['3','03']:
		exit()
	else:
		print('jangan kosong bg')
		os.system('python run.py')


if __name__=='__main__':
  login()
