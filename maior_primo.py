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
