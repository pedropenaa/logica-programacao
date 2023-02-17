import Jogos.forca as forca
import Jogos.adivinha as adivinha
import Jogos.bolinha as bolinha


def escolhe_jogo():
    print("VAMOS ESCOLHER O JOGO")

    print("(1) adivinhação")
    print("(2) Forca")
    print("(3) Bolinha")

    jogo = int(input("Qual jogo deseja jogar: "))


    if jogo == 1:
        print("jogando o jogo da adivinhação")
        adivinha.jogar_advinhacao()

    elif jogo == 2:
        print("Jogando o jogo da forca")
        forca.jogar_forca()

    elif jogo == 3: 
        print("jogando o jogo da bolinha")
        bolinha.jogar_bolinha()
    else: 
        print("Esse jogo nao existe!!, POR FAVOR ESCOLHA OUTRO")



if __name__ == "__main__":
    escolhe_jogo()
    