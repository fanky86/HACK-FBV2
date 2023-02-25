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


try:
	import rich
	sue='# module rich telah terinstall...'
	sui=mark(sue,style='green')
	sol().print(sui,style='cyan')
except ImportError:
	sup='# module rich belum terinstall...'
	suo=mark(sup,style='green')
	sol().print(suo,style='cyan')
	os.system('pip install rich')
	
try:
	import ruby
	sul='# module ruby belum terinstall...'
	syu=mark(sul,style='green')
	sol().print(syu,style='cyan')
except ImportError:
	suq='# module ruby belum terinstall...'
	suh=mark(suq,style='green')
	sol().print(suh,style='cyan')
	os.system('pkg install ruby -y')
