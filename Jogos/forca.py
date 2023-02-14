


def jogar_forca():
    palavra_secreta = "banana"
    enforcou        = False
    acertou         = False
    
    #enquanto nao enforcou e nao acertou a palavra secreta 
    while not enforcou  and not acertou:
        chute = str(input("Qual letra?"))
        index = 0 
        for letra in palavra_secreta:
            if chute == letra:
                print(f"Encontrei a letra {chute.upper()} na posisão {index}")
                index += 1 



