"""
Exercício 1
Escreva um programa que recebe como entradas (utilize a função input) dois números inteiros correspondentes à largura e à altura de um retângulo, respectivamente.
O programa deve imprimir uma cadeia de caracteres que represente o retângulo informado com caracteres '#' na saída.

digite a largura: 10
digite a altura: 3
##########
##########
##########


digite a largura: 2
digite a altura: 2
##
##

"""

l = int(input('digite a largura:'))
a = int(input('digite a altura:'))


while a > 0:
    print(l*'#')
    a -= 1
    
