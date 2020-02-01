import os 
import socket
x=1
clear='clear'#limpar terminal
menud='python3 main.py'
while (x==1):
  print("")
  print("Ip: "+socket.gethostbyname(socket.gethostname()))
  print("=========================")
  print("")
  print("1.Ipconfig")
  print("2.Verificar Portas")
  print("3.Ip Externo")
  print('4.Testa Velocidade da internet')
  print('5.Voltar para menu inicial')
  print("")
  print("=========================")
  opcao=(input("Escolha Opção:"))
  os.system(clear)
  if opcao == '1':
    ipconfig='ifconfig'
    os.system(ipconfig)
  if opcao == '2':
    porta=(input("Ip ou Url para verificar portas:"))
    nmap='nmap'
    nporta='nmap '+'porta'
    print(nporta)
    os.system(nporta)
  if opcao == '3':
    ipex='links ipinfo.io/ip'
    os.system(ipex)
  if opcao == '4':
    speed="./speedtest-cli"
    os.system(speed)
  if opcao == '5':
    menud='python3 main.py'
    os.system(menud)
    x=2
  else:
    print(opcao)
    os.system(opcao)