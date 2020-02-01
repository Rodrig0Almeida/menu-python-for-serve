import os 
x=1
clear='clear'#limpar terminal
menud='python3 main.py'
while (x==1):
  print('')
  print("Descompactar      ")
  print("=========================")
  print("")
  print("1.ZIP")
  print("2.RAR")
  print('3.Voltar para menu inicial')
  print("")
  print("=========================")
  opcao=(int(input("Escolha Opção:")))
  os.system(clear)
  if opcao ==1:
    print('ZIP')
  if opcao ==2:
    print('RAR')
  if opcao ==1 or opcao ==2:
    print('Coloque o local por completo *ex: /home/usuario/pasta')
    print("=========================")
    local=(input("Coloque local do arquivo: "))
    arquivo=(input("Coloque nome do arquivo: "))
    destino=(input("Coloque local de extração: "))
    print("=========================")
    rar='unrar x "'+local+'/'+arquivo+'" -d '+'"'+destino+'"'
    zipe='unzip "'+local+'/'+arquivo+'" -d '+'"'+destino+'"'
    if opcao == 1:
     print('unzip "'+local+'/'+arquivo+'" -d '+'"'+destino+'"')
     os.system(zipe)
     
    if opcao == 2:
     print('unrar x "'+local+'/'+arquivo+'" -d '+'"'+destino+'"')
     os.system(rar)
  if opcao == 3:
    os.system(menud)
    x=2