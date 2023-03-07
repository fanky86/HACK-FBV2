import os,json,time
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

os.system('clear')
def login():
	sholat()

def clear():
	os.system('clear')
		
def subuh():
				oss='latin : Ushalli fardhosh shubhi rok`ataini mustaqbilal qiblati adaa-an lillaahi ta`aala\n\nTranslation_id : Aku berniat shalat fardhu Shubuh dua raka`at menghadap kiblat karena Allah Ta`ala'
				pol=nel(oss,style='green')
				cetak(nel(pol,style='cyan',title='NIAT SHOLAT SUBUH'))

def dzuhur():
				sky='latin : Ushalli fardhodl dhuhri arba`a raka`aatim mustaqbilal qiblati adaa-an lillaahi ta`aala,\n\ntranslation_id : Aku berniat shalat fardhu Dzuhur empat raka`at menghadap kiblat karena Allah Ta`ala'
				poo=nel(sky,style='green')
				cetak(nel(poo,style='cyan',title='NIAT SHOLAT DZUHUR'))
				
def ashar():
				sky='latin": "Ushalli fardhol `ashri arba`a raka`aatim mustaqbilal qiblati adaa-an lillaahi ta`aala,\n\ntranslation_id": "Aku berniat shalat fardhu `Ashar empat raka`at menghadap kiblat karena Allah Ta`ala'
				poo=nel(sky,style='green')
				cetak(nel(poo,style='cyan',title='NIAT SHOLAT ASHAR'))


def magrib():
				sky='latin : Ushalli fardhol maghribi tsalaata raka`aatim mustaqbilal qiblati adaa-an lillaahi ta`aala,\n\ntranslation_id": "Aku berniat shalat fardhu Maghrib tiga raka`at menghadap kiblat karena Allah Ta`ala'
				poo=nel(sky,style='green')
				cetak(nel(poo,style='cyan',title='NIAT SHOLAT MAGRIB'))
				

def isak():
				sky='latin : Ushalli fardhol `isyaa-i arba`a raka`aatim mustaqbilal qiblati adaa-an lillaahi ta`aala,\n\ntranslation_id : Aku berniat shalat fardhu Isya empat raka`at menghadap kiblat karena Allah Ta`ala'
				poo=nel(sky,style='green')
				cetak(nel(poo,style='cyan',title='NIAT SHOLAT ISAK'))
				
				
				
class sholat:
	oss='[1] SHOLAT SUBUH\n[2] SHOLAT DZUHUR\n[3] SHOLAT ASHAR\n[4] SHOLAT MAGRIB\n[5] SHOLAT ISYA`\n[6] BACK'
	pos=nel(oss,style='green')
	cetak(nel(pos,style='cyan',title='PILIHAN NIAT SHOLAT'))
	usna = input('pilih nomor : ')
	if usna in ['1','01']:
		subuh()
	elif usna in ['2','02']:
		dzuhur()
	elif usna in ['3','03']:
		ashar()
	elif usna in ['4','04']:
		magrib()
	elif usna in ['5','05']:
		isak()
	elif usna in ['6','06']:
		from src import asset.cok
	else:
		print('\x1b[1;91mwrong input [!!!]')
		from src import Data
		
if __name__=='__main__':
	login()
