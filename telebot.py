import os
import shutil
x = 1
clear = 'clear'  #limpar terminal
reboot = 'sudo reboot'
htop = 'htop'  #abrir htop
while (x == 1):
  print('')
  print("Telebot v5       ")
  total2, used2, free2 = shutil.disk_usage("/")
  print("======================")
  print("|Interna   Free: %d GB  " % (free2 // (2**30)))
  print("======================")
  print("|1.Processos         ")
  print('|2.Download          ')
  print('|3.Menu de funções   ')
  print("|4.Reiniciar servidor")
  print("======================")
  opcao = (input("Escolha Opção:"))
  if opcao == "1" or opcao == "htop":
    os.system(htop)
    os.system(clear)
  if opcao == '2':
    mnt=input("Local de Download:")
    link=input("Coloque link: ")
    baixa1 ='aria2c -d '+mnt+' --seed-time=0 --seed-ratio=0.0'+' "'+link+'"'
    os.system(baixa1)
    os.system(clear)
  if opcao == '3':
    menu="python3 main.py"
    os.system(menu)
    x=2
  if opcao == '4' or opcao == 'reboot':
    os.system(reboot)
  else:
    os.system(opcao)