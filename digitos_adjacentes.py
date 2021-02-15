# Entrando com um número inteiro
num=int(input('Digite um número inteiro: '))

# Gerando resto inicial da divisão
rest1=num%10

if (num // 2) >= 5: # Condicional para quando digitarem números abaixo de 10
      while num // 10 !=0: # Rode até que a variável num seja igual a zero
            num = num // 10
            rest = num % 10
            if rest == rest1:
                  print('sim')
                  break
            rest1 = rest
            if num // 10 == 0:
                  print('não')
else:
      print('não')
