import os
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
try:
	import rich
	sue='# module rich telah terinstall...'
	sui=mark(sue,style='green')
	sol().print(sui,style='cyan')
except ImportError:
	sup='# module rich belum terinstall...'
	suo=mark(sup,style='red')
	sol().print(suo,style='cyan')
	os.system('pip install rich')
	
try:
	import bs4
	sul='# module bs4 telah terinstall...'
	syu=mark(sul,style='green')
	sol().print(syu,style='cyan')
except ImportError:
	suq='# module bs4 belum terinstall...'
	suh=mark(suq,style='green')
	sol().print(suh,style='cyan')
	os.system('pip install bs4')
	dog='# succes install module bs4...'
	dof=mark(dog,style='green')
	sol().print(dof,style='cyan')
