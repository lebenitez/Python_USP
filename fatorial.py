n = int(input('Digite o valor de n: '))

nfat = n
fat = n - 1


while fat >= 1:
      nfat = nfat * fat
      fat -= 1
print(nfat)
