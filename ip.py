import os 
import socket
x=1
clear='clear'#limpar terminal
menud='python3 main.py'
while (x==1)
  os.system(clear)
  print("")
  print("Ip: "+socket.gethostbyname(socket.gethostname()))
  print("=========================")
  print("")
  print("1.Ipconfig")
  print("2.Verificar Portas")
  print('3.Voltar para menu inicial')
  print("")
  print("=========================")
  opcao=(int(input("Escolha Opção:")))
  os.system(clear)
  if opcao == 1:
    ipconfig='ifconfig'
    os.system(ipconfig)
  if opcao == 2:
    porta=(input("Ip ou Url para verificar portas:"))
    nmap='nmap'
    nporta='nmap '+'porta'
    print(nporta)
    os.system(nporta)
  if opcao == 3:
    menud='python3 main.py'
    os.system(menud)
    x=2
  if opcao == 69:
    import urllib.request
    pagina = urllib.request.urlopen("http://www.meuip.com.br/index.php")
    texto = pagina.read().decode("utf8")
    busca = texto.find('div_ip").innerHTML = "')
    inicio = busca + 22
    final = texto[inicio:]
    final = final.find('"')
    final = inicio + final
    ip = texto[inicio:final]
    print (ip)
