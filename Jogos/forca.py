

def jogar_forca():
    palavra_secreta = "banana".upper()
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]


    enforcou        = False
    acertou         = False
    tentativa       = 0 

    
    print(letras_acertadas)

    #enquanto nao enforcou e nao acertou a palavra secreta 
    while not enforcou  and not acertou:

        chute = str(input("Qual letra: "))
        chute = chute.strip().upper()
         
        if chute in palavra_secreta:
            index = 0 
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[index] = letra
                index += 1 
        else: 
            tentativa += 1 

        enforcou = tentativa == 6
        acertou = "_" not in letras_acertadas
      



    print(letras_acertadas)

    if acertou:
        print("Você ganhou!!!")
    else:
        print("Você perdeu")



    print("FIM DE JOGO!!!!!")




if __name__ == "__main__":
    jogar_forca()