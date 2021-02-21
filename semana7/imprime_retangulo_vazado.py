"""
Refaça o exercício 1 imprimindo os retângulos sem preenchimento, de forma que os caracteres que não estiverem na borda do retângulo sejam espaços.

Por exemplo:

digite a largura: 10
digite a altura: 3
##########
#        #
##########

digite a largura: 2
digite a altura: 2
##
##


"""
l = int(input('digite a largura:'))
a = int(input('digite a altura:'))


a -= 2
print(l*'#')
while a > 0:
    print('#' + ((l - 2) * ' ') + '#')
    a -= 1
print(l*'#')
    
