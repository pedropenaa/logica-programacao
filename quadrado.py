
lado = int(input("Quantos caracteres no lado do quadrado [10-100]? "))

if lado < 10 or lado > 100:
  print ("Informe um número entre 1 e 100!")

else:
  for linha in range(0, lado):
      print()

      for coluna in range(0, lado):
          if linha == coluna or linha + coluna == lado - 1:
               print(" + ", end="")
          else:
              print(" 0 ", end="")
