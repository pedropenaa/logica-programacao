from graphics import *
import random


win = GraphWin("Bolinha ...", 800, 600)

linhaSuperior = Line(Point(0, 40), Point(800, 40))
linhaSuperior.setWidth(10)
linhaSuperior.setFill(color_rgb(10, 100, 10))
linhaSuperior.draw(win)

linhaInferior = Line(Point(0, 550), Point(800, 550))
linhaInferior.setWidth(3)
linhaInferior.setFill(color_rgb(10, 100, 10))
linhaInferior.draw(win)

col = 390
lin = 60
circulo=Circle(Point(col, lin), 15)
circulo.setFill(color_rgb(10, 10, 100))
circulo.draw(win)

pontos=Text(Point(400, 575), "Pontos: 0")
pontos.setSize(14)
pontos.draw(win)

colIni = 340
barra=Line(Point(colIni, 530), Point(colIni+100, 530))
barra.setFill(color_rgb(100, 10, 10))
barra.setWidth(10)
barra.draw(win)

velocidade=10
bateu = True
continuar = True
while continuar:

  if bateu:
      passo = int(random.random()*20)+1
      bateu = False





  if (col + passo) > 800:
      passo = -passo

  if (-col - passo)< 0 :
      passo= +passo
  # Nova posição do círculo
  circulo.undraw()
  col += passo
  lin += velocidade
  circulo = Circle(Point(col, lin), 15)
  circulo.setFill(color_rgb(10, 10, 100))
  circulo.draw(win)

  # Movimento horizontal da barra pelas setas direita/esquerda
  tecla = win.checkKey()

  # Sair do joguinho
  if tecla == "Escape":
      continuar = False
      continue

  if tecla == "Right":

     if (colIni + 20) < 701:
       colIni = colIni + 20

     barra.undraw()
     barra = Line(Point(colIni, 530), Point(colIni + 100, 530))
     barra.setFill(color_rgb(100, 10, 10))
     barra.setWidth(10)
     barra.draw(win)


  if tecla == "Left":
      if (colIni - 20) > -1:
          colIni = colIni - 20

      barra.undraw()
      barra = Line(Point(colIni, 530), Point(colIni + 100, 530))
      barra.setFill(color_rgb(100, 10, 10))
      barra.setWidth(10)
      barra.draw(win)




  if col > colIni and col<(colIni+100) and  (lin+15)>= 530:
      velocidade= - velocidade

  # Esperar o ser humano reagir
  time.sleep(.07)

win.close()

