print("**********************************")
print("Bem Vindo ao jogo de Advinhação!"  )
print("**********************************")
print("O NUMERO SECRETO ESTA ENTRE: 0-10" )



numero_secreto  = 9
tentantiva = 5
rodada = 1 




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

 

   






