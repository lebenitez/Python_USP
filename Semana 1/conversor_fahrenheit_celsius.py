"""Conversos de Fahrenheit para Celsius"""

temp_Fahrenheit = int(input('Digite a temperatura em Fahrenheit: '))

# Armazena em variável o resultado da operação de conversão de Fahrenheit para Celsius
# Na operação de divisão, utilizei o // para que o resultado seja um inteiro e não um float.
temp_Celsius = (temp_Fahrenheit - 32) * 5 // 9

print('A temperatura em Celsius é de', temp_Celsius,'graus.')
