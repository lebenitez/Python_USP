# Entrando com um número inteiro
num=int(input('Digite um número inteiro: '))

# Gerando resto inicial da divisão
rest1=num%10


while num // 10 !=0: # Rode até que a variável num seja igual a zero
      num = num // 10
      rest = num % 10
      if rest == rest1:
            print('sim')
            break
      rest1 = rest
if num // 10 == 0 and rest != rest1:
      print('não')

