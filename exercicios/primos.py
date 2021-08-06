
n = int(input('Digite um número inteiro positivo:'))
i = 2
resultado = 0
while (i <= (n/2)):
    while ((n % i)==0):
        resultado = resultado + 1
        break
    i = i + 1
if (resultado == 0):
    print('O número',n,'É um número primo.')
else:
    print('O número', n, 'NÃO É um número primo.')