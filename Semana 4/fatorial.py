"""
Escreva um programa que receba um número natural  n n na entrada e imprima  n! n! (fatorial) na saída.
"""

# Descomentar caso vá usar a função factorial do módulo math
# import math

n = int(input('Digite o valor de n: '))

""" A coisa toda pode ser feita de forma bem simples com a função factorial do módulo math """
# Descomentar a linha abaixo caso prefira usar a função factorial no lugar do código da linha 14
#print(math.factorial(n))

""" Mas só descobri a função acima depois de tomar um pão para fazer a função abaixo.
O bom de ter quebrado a cabeça com a função abaixo foi que me obriguei a utilizar o modo debugger e isso terminou me ajudando a raciocinar melhor.
"""

nfat = n
fat = n - 1

if n == 0:
      print(1)
else:
      while fat >= 1:
            nfat = nfat * fat
            fat -= 1
      print(nfat)


