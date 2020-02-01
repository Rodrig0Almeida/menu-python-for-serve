import os 
x=1
clear='clear'#limpar terminal
tmux="tmux"# abre tmux
tmuxd='tmux detach'#tira o processo da sua sessão
tmuxa='tmux attach'#coloca ele de novo na sua sessão
menud="python3 main.py"
while (x==1):
  print("Tmux    ")
  print("Menu para usar no terminal *não usar no tmux")
  print("para abri o terminal no tmux aperte Ctrl B %")
  print("=========================")
  print("")
  print("1.Abri tmux(tmux)")
  print("2.Fechar tmux(tmux detach)")
  print("3.Abri processo tmux(tmux attach)")
  print('4.Voltar para menu inicial')
  print('')
  print("=========================")
  opcao=(int(input("Escolha Opção:")))
  os.system(clear)
  if opcao == 1:
    os.system(tmux)
  if opcao == 2:
    os.system(tmuxd)
  if opcao == 3:
    os.system(tmuxa)
  if opcao == 4:
    os.system(menud)
    x=2