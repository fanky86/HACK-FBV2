import requests,json,bs4,time,re,os
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

try:
    	IP = requests.get('https://api.ipify.org/').text
    	sky='# YOUR ALAMAT IP : %s'%(IP)
    	sky2=mark(sky,style='green')
    	sol().print(sky2,style='cyan')
    	try:
    		ski='# 1.OPEN'
    		ski2=mark(ski,style='green')
    		sol().print(ski2,style='cyan')
    		try:
    			sue='# 2.KELUAR'
    			sue2=mark(sue,style='green')
    			sol().print(sue2,style='cyan')
    		except IOError:
    			print()
    	except IOError:
    		print('gae lo')
except IOError:
    	print()
    	
    	
usna = input('nomor:')
if usna == '1':
	print('succes')
elif usna == '2':
	exit()
