def soma(a,b):
    return a + b

def subtracao(a,b):
    return a - b

def divisao(a,b):
    return a / b

def multiplicacao(a,b):
    return a * b


def calculadora():

    print("Vamos Começar!!!!!")
    print("Escolha qual conta deseja fazer:  ")
    print(" 1 - Soma          ")
    print(" 2 - Subtração     ")
    print(" 3 - Divisão       ")
    print(" 4 - Multiplicação ")



    escolha = int(input("Qual sua escolha de hoje: "))
    numero1 = int(input("Qual o primeiro numero:   "))
    numero2 = int(input("Qual o segundo  numero:   "))


    if escolha == 1 :
        print(soma(numero1, numero2))
    elif escolha == 2:
        print(subtracao(numero1, numero2))
    elif escolha == 3:
        if numero2 == 0:
            print("Impossivel fazer divisao por 0")
        else:
            print(divisao(numero1, numero2))

    else:
        print(multiplicacao(numero1, numero2))



if __name__ == "__main__":
    calculadora()

