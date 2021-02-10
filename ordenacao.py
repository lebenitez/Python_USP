"""
Receba 3 números inteiros na entrada e imprima crescente se eles forem dados em ordem crescente. Caso contrário, imprima não está em ordem crescente
 
"""

primeiro_numero = int(input('Digite o primeiro número inteiro: '))
segundo_numero = int(input('Digite o segundo número inteiro: '))
terceiro_numero = int(input('Digite o terceiro número inteiro: '))

if primeiro_numero < segundo_numero and segundo_numero < terceiro_numero:
      print('crescente')
else:
      print('não está em ordem crescente')
