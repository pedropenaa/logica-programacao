

linhas = int(input("Quantas linhas no triângulo [10-100]? "))

if linhas < 10 or linhas > 100:
  print("Informe um número entre 1 e 100!")

else:
  qtd = linhas

  for lin in range(0, linhas):
      print()
      inicio = int ( linhas / 2) - int ( qtd / 2)

      for col in range( 0, inicio + qtd):
          if col < inicio:
              print("   ", end="")

          else:
              print(" 0 ", end="")
      qtd-=1
