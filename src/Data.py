import os,requests

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
  sue='# 1.open'
  hud='# 2.exit'
  sul=mark(sue,hud,style='green')
  sol().print(sul,style='cyan')
  usna = input('pilih nomor:')
  if usna == '1':
    try:
      os.system('xdg-open https://google.com')
    except IOError:
      print('masuk error')
      
  elif usna == '2':
    exit('thank bro')
  else:
    print('masukan nomor yang benar bro')
    
    
if __name__=='__main__':
  update()
  clear()
  login()
