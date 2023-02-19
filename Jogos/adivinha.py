import random

def jogar_advinhacao():

     print("**********************************")
     print("Bem Vindo ao jogo de Advinhação!"  )
     print("**********************************")
     print("O NUMERO SECRETO ESTA ENTRE: 1-15" )
     print("**********************************")



     numero_secreto  = random.randint(1,15)
     tentantiva = 0
     rodada = 1 

     #print(numero_secreto)

     print("*****************************************")

     print("Defina o nivel da dificuldade")

     print( "(1) Fácil"   )
     print( "(2) Medio"   )
     print( "(3) Difícil" )



     nivel = int(input("Qual o nivel de dificuldade desejado: "))


     if nivel == 1:
          tentantiva= 20 
     elif nivel == 2:
          tentantiva = 10
     else:
          tentantiva = 5 




     while rodada <= tentantiva:
          print("Tentativa {} de {}".format(rodada, tentantiva))
          adivinha = int(input("Qual o numero do chute: "))

          acertou = adivinha == numero_secreto
          maior   = adivinha > numero_secreto
          menor   = adivinha < numero_secreto



          if acertou:
               print("PARABENS!!!!!! Você acertou o numero!!!!!")
               break
          
          else:
               if maior:
                print("Seu numero foi maior que o numero secreto!")

               elif menor:
                    print("Seu numero foi menor que o numero serecto")
                    
          rodada += 1   


     print("FIM DE JOGO!!!!!") 

 

   






