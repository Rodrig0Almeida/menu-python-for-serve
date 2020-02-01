import os
import socket
x=1
clear='clear'#limpar terminal
menud='python3 main.py'
while (x==1):
  print('')
  print ("Download     ")
  print("=========================")
  print("")
  print("1.Download")
  print("2.Download em segundo plano")
  print('3.Voltar para menu inicial')
  print("")
  print("=========================")
  opcao=(input("Escolha Opção:"))
  os.system(clear)
  if opcao =='1':
    print('Download')
  if opcao =='2':
    print('Download em segundo plano')
  if opcao =='1' or opcao =='2':
    print('Donwload')
    print("=========================")
    local=input("Coloque local de Download do arquivo: ")
    link=input("Coloque link: ")
    print("=========================")
    baixa1 ='aria2c -d '+local+' --seed-time=0 --seed-ratio=0.0'+' "'+link+'"'
    baixa2='nohup aria2c -d '+local+' --seed-time=0 --seed-ratio=0.0'+' "'+link+'"'+'&'

    if opcao == '1':
     print('aria2c -d '+local+' --seed-time=0 --seed-ratio=0.0'+' "'+link+'"')
     os.system(str(baixa1))
     
    if opcao == '2':
     print('nohup aria2c -d "'+local+' --seed-time=0 --seed-ratio=0.0'+' "'+link+'"'+'&')
     os.system(baixa2)
     
  if opcao == '3':
    os.system(menud)
    x=2
  else:
    print(opcao)
    os.system(opcao)