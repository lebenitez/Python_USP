import math

a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))

# Calculando o Delta
delta = b ** 2 - 4 * a * c

# Calculando a raiz quadrada

if delta == 0:
      raiz1 = (-b + math.sqrt(delta))/(2 * a)
      print('A única raiz é: ', raiz1)
else:
      if delta < 0:
            print('Esta equação não possui raizes reais.')
      else:
            raiz1 = (-b + math.sqrt(delta))/(2 * a)
            raiz2 = (-b - math.sqrt(delta))/(2 * a)
            print('A primeira raiz é: ', raiz1)
            print('A segunda raiz é: ', raiz2)
