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

def update():
  os.system('git pull')
def clear():
  os.system('clear')
def login():
  menu()
def banner():
	print('''
      	_______           ______   _______  _                 ______  
       (  ____ )|\     /|(  __  \ (  ___  )( \      |\     /|(  __  \ 
       | (    )|| )   ( || (  \  )| (   ) || (      ( \   / )| (  \  )
       | (____)|| |   | || |   ) || (___) || | _____ \ (_) / | |   ) |
       |     __)| |   | || |   | ||  ___  || |(_____) ) _ (  | |   | |
       | (\ (   | |   | || |   ) || (   ) || |       / ( ) \ | |   ) |
       | ) \ \__| (___) || (__/  )| )   ( || (____/\( /   \ )| (__/  )
       |/   \__/(_______)(______/ |/     \|(_______/|/     \|(______/ 
       ''')
class menu:
  banner()
  sue='[1] OPEN\n\[2] KEPO\n[3] EKIT'
  sul=nel(sue,style='green')
  cetak(nel(sul,style='red',title='PILIHAN MENU'))
  usna = input('pilih nomor : ')
  if usna in ['1','01']:
  	os.system('xdg-open https://google.com')
  elif usna in ['2','02']:
  	print('kepo amat Lo wkwk')
  elif usna in ['3','03']:
        exit()
if __name__=='__main__':
  update()
  clear()
  login()
