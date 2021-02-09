"""
Faça um programa em Python que receba quatro notas, calcule e imprima a média aritmética. Observe o exemplo abaixo:

Exemplo:

Entrada de Dados:
Digite a primeira nota: 4

Digite a segunda nota: 5

Digite a terceira nota: 6

Digite a quarta nota: 7

Saída de Dados:
A média aritmética é 5.5
"""

primeira_nota = float(input('Digite a primeira nota: '))
segunda_nota = float(input('Digite a segunda nota: '))
terceira_nota = float(input('Digite a terceira nota: '))
quarta_nota = float(input('Digite a quarta nota: '))

print('A média aritmética é', (primeira_nota + segunda_nota + terceira_nota + quarta_nota) / 4)
