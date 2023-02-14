import Jogos.forca as forca
import Jogos.adivinha as adivinha


def escolhe_jogo():
    print("VAMOS ESCOLHER O JOGO")

    print("(1) adivinhação")
    print("(2) Forca")

    jogo = int(input("Qual jogo deseja jogar: "))


    if jogo == 1:
        print("jogando o jogo da adivinhação")
        adivinha.jogar_advinhacao()

    elif jogo == 2:
        print("Jogando o jogo da forca")
        forca.jogar_forca()

    else: 
        print("esse jogo nao existe")


if __name__ == "__main__":
    escolhe_jogo()
    