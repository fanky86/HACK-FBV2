import os,requests

def update():
  os.system('git pull')
def clear():
  os.system('clear')
def login():
  menu()
  
  banner=('OPEN WAR')
  
class menu:
  print(f"""{banner}
        1.open
        2.keluar""")
  usna = input('pilih nomor:')
  if usna == '1':
    try:
      open=requests.get('https://google.com')
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
