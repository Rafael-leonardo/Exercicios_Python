import math

a = int(input('Qual o valor de a? '))
b = int(input('Qual o valor de b? '))
c = int(input('Qual o valor de c? '))

print(a, 'x² +', b, 'x +', c)

Delta = (b ** 2) - 4 * a * c

if Delta > 0:
    x1 = (- b + math.sqrt(Delta)) / (2 * a)
    x2 = (- b - math.sqrt(Delta)) / (2 * a)
    if x1 > x2:
        print(x2, 'e', x1)
    elif x2 > x1:
        print(x1, 'e', x2)
    else:
        print('as duas raízes é', x1)
else:
    print('não tem raízes nesta equação')