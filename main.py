import os
x = 1
tele = 'python3 telebot.py'
ip = 'python3 ip.py'
clear = 'clear'  #limpar terminal
winrar = 'python3 winrar.py'  #ww arquivo .py do menu de descompactação
reboot = 'sudo reboot'
htop = 'htop'  #abrir htop
down = 'python3 download.py'  #dd arquivo .py do menu de download
tmux = 'python3 tmux.py'  #abri tmux
secreto = 'python3 secreto.py'
os.system(clear)
while (x == 1):
  print('')
  print('Menu de Funções v5')
  print("=========================")
  print("")
  print("1.Descompactar arquivos")
  print("2.Monitorar processos")
  print("3.Download")
  print("4.Tmux")
  print('5.Ip')
  print('6.Telebot')
  print("7.Reiniciar servidor")
  print("")
  print("=========================")
  opcao = (input("Escolha Opção:"))
  os.system(clear)
  if opcao == '1':
    os.system(winrar)
    x = 2  #para fechar o while
  if opcao == '2':
    os.system(htop)
  if opcao == '3':
    os.system(down)
    x = 2  #para fechar o while
  if opcao == '4':
    os.system(tmux)
    x = 2
  if opcao == '5':
    os.system(ip)
    x = 2
  if opcao == '6':
    os.system(tele)
    x = 2
  if opcao == '7':
    os.system(reboot)
  if opcao == '14':
    os.system(secreto)
    x = 2
  else :
    print(opcao)
    os.system(opcao)
