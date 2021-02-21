"""
Receba um número inteiro positivo na entrada e imprima os  n n primeiros números ímpares naturais. Para a saída, siga o formato do exemplo abaixo.
"""

n = int(input('Digite o valor de n: '))
i = 0
x = 1

while i < n:
      if x % 2 != 0:
            print(x)
            i += 1
            x += 1
      else:
            x += 1


      
