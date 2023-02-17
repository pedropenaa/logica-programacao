#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius

temp = int(input("Qual temperatura em Fahrenheit deseja transformar em Celsius: "))

celsius = 5 * ((temp - 32) / 9 )

print(f"Sua temperatura de  {temp}°F, em Celsius é de, {round(celsius) } °C!")