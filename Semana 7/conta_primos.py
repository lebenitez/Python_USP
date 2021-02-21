"""
Escreva a função n_primos que recebe como argumento um número inteiro maior ou igual a 2 como parâmetro e devolve a quantidade de números primos
que existem entre 2 e n (incluindo 2 e, se for o caso, n).

>>>n_primos(2)
1
>>>n_primos(4)
2
>>>n_primos(121)
30

"""


def primo(k):
      """
      Verifica se um número inteiro é ou não primo.
      """
      mult = 0

      if k == 1:
            print('não primo')
      else:
            for count in range(2, k):
                  if (k % count == 0):
                        mult += 1


            if mult == 0:
                  #print('primo')
                  return 'primo'
            else:
                  #print('não primo')
                  return 'não primo'


def maior_primo(x):
      """
      Utiliza um laço while junto com a função primo para chegar o maior número primo antes de x.
      """
      while x > 2:
            if primo(x) == 'primo':
                  return x                  
            else:
                  x -= 1

def n_primos(n):
      totPrimos = 0
      while n >= 2:
            if primo(n) == 'primo':
                  totPrimos += 1
                  n -= 1
            else:
                  n -= 1
      return totPrimos
                  
      
