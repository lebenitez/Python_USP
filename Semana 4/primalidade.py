num = int(input('Digite um número inteiro: '))
mult = 0

if num == 1:
      print('não primo')
else:
      for count in range(2, num):
            if (num % count == 0):
                  mult += 1


      if mult == 0:
            print('primo')
      else:
            print('não primo')
