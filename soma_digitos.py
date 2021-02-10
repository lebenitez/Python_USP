"""
Escreva um programa que receba um número inteiro na entrada, calcule e imprima a soma dos dígitos deste número na saída.
"""

numero = int(input('Digite um número inteiro: '))
div = numero // 10
x = 0
i = 0

while div > 0:
      x = x + (numero % 10)
      numero = div
      if (div / 2) < 5 and i != 1:
            div += 1
            i += 1
      else:
            div = div // 10
print(x)
