import os 
x=1
clear='clear'#limpar terminal
tshell="python3 tshell.py"
menud="python3 main.py"
install='sudo apt-get install aria2 & sudo apt-get install tmux & sudo apt-get install unrar'
while (x==1):
  print('')
  print ("Menu Secreto    ")
  print("=========================")
  print("")
  print("Obrigado a todo que ajudarão")
  print("Creditos")
  print("@AlmeidaRodrigo")
  print("@soru98")
  print('@VegaZS')
  print('@EsdrasTarsis')
  print("@caiosy")
  print('')
  print("1.tshell.py by @soru98 ")
  print("2.Voltar para menu inicial")
  print("")
  print("=========================")
  opcao=(int(input("Escolha Opção:")))
  os.system(clear)
  if opcao == 1:
    os.system(tshell)
  if opcao == 2:
    os.system(menud)