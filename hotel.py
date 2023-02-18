
#No hotel morte lenta, estavam hospedados 5 hospédes, Renato Faca, Maria Cálice, Roberto Arma, Roberta Corda e Uesllei.

#A meia noite, o hóspede do quarto 101 foi encontrado morto e os 5 suspeitos são os citados acima.

#Descubra quem é o assassino sabendo que:

 #Se o nome do suspeito contem 3 vogais ou mais(Nome completo) e nenhuma dessas vogais é u ou o, ele pode ser o assassino.X

#Se o suspeito for do sexo feminino, só sera assassina se tiver utilizado uma arma branca.
# #Se o suspeito for do sexo masculino, ele deveria estar no saguão do hotel a 00h30 para ser considerado o assasino.

 #Sabendo dessas informações acima, projete o algorítmo que fornecido o nome do suspeito, indique se ele pode ou não ser o assassino.


male = ["Renato Faca","Roberto Arma", "Uesllei"]
female= ["Maria Calice", "Roberta Corda"]
total = ["Roberto Faca","Roberto Arma", "Uesllei","Maria Calice", "Roberta Corda"]
contadorDeVogais = 0
whitegun= ["faca", "corda","calice" ]
Haswhitegun= False



for i in range(len(total)):
  print(str(i+1)+" - "+total[i])
posicao = input("write the number of suspect: ")
name = total[int(posicao)-1]

for a in name:
 if a in "aei":
     contadorDeVogais+=1

if contadorDeVogais >= 3 and "o" not in name.lower() and "u" not in name.lower():
  print(name, " é  guilty")

for b in whitegun:
  if b in name.lower():
      temArmaBranco = True

if name in female and Haswhitegun:
  print(name, " é  guilty")

if name in male:
  lobby= input("was he in the lobby at 00h?")
  if lobby=="yes".replace(" ",""):
      print(name, " é guilty")


