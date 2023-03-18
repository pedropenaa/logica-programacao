''' tabuada de algum numero escolhido pelo usuario, ate 10 '''

numero = int(input("Digite um numero de 1 a 10: "))
for i in range(1, 11):
    print(f"{numero} X {i} = {numero * i}")
