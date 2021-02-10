"""
Receba 4 números na entrada, um de cada vez. Os dois primeiros devem corresponder, respectivamente, às coordenadas x e y de um ponto em um plano cartesiano.
Os dois últimos devem corresponder, respectivamente, às coordenadas x e y de um outro ponto no mesmo plano.

Calcule a distância entre os dois pontos. Se a distância for maior ou igual a 10, imprima

longe

na saída. Caso o contrário, quando a distância for menor que 10, imprima

perto
 
​	
"""
import math

numero1 = int(input('Digite a primeira coordenada: '))
numero2 = int(input('Digite a segunda coordenada: '))
numero3 = int(input('Digite a primeira coordenada do novo plano cartesiano: '))
numero4 = int(input('Digite a segunda coordenada do novo plano cartesiano: '))

# Calculando a distância
distancia = math.sqrt((numero1-numero2)**2) + ((numero3-numero4)**2)

if distancia > 10:
      print('longe')
else:
      print('perto')

