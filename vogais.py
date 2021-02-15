"""
Escreva a função vogal que recebe um único caractere como parâmetro e devolve True se ele for uma vogal e False se for uma consoante.

Exemplos de execução no shell de Python


>>> vogal("a")
True
>>> vogal("b")
False
>>> vogal("E")
True

"""

vogais = ['a','A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']

def vogal(x):
      for i in vogais:
            if x in vogais:
                  return True
            else:
                  return False


# Testes automatizados com pytest
def teste_vogala():
      assert vogal('a') == True
def teste_vogalA():
      assert vogal('A') == True
def teste_vogalo():
      assert vogal('o') == True
def teste_vogalU():
      assert vogal('U') == True
def teste_consoantec():
      assert vogal('c') == False
def teste_consoantep():
      assert vogal('p') == False
def teste_consoantez():
      assert vogal('z') == False
      
