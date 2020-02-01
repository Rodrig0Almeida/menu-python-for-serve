import os 
x=1
clear='clear'#limpar terminal
winrar='python3 winrar.py'#ww arquivo .py do menu de descompactação
reboot='sudo reboot'
htop='htop'#abrir htop
down='python3 download.py'#dd arquivo .py do menu de download
tmux='python3 tmux.py'#abri tmux
secreto='python3 secreto.py'
while (x==1):
  print ("Menu de Funções v7    ")
  print("=========================")
  print("")
  print("1.Descompactar arquivos")
  print("2.Monitorar processos")
  print("3.Download")
  print("4.Tmux")
  print("5.Reiniciar servidor")
  print("")
  print("=========================")
  opcao=(int(input("Escolha Opção:")))
  print("=========================")
  os.system(clear)
  if opcao == 1:
    os.system(winrar)
    x=2#para fechar o while
  if opcao == 2:
    os.system(htop)
  if opcao == 3:
    os.system(down)
    x=2#para fechar o while
  if opcao == 4:
    os.system(tmux)
    x=2
  if opcao == 56:
      local=input("nome usuario:")
      link=input("link da atualização:")
      att='rm /home/'+local+'/menu.zip && '+'aria2c -d '+'/home/'+local+' --seed-time=0 --seed-ratio=0.0'+' "'+link+'"'+' && '+'unzip "'+'/home/'+local+' -d '+'/home/'+local+' && '+' rm /home/'+local+'/menu.zip'
      os.system(att)
  if opcao == 5:
    os.system(reboot)
  if opcao == 69:
    os.system(secreto)
    x=2