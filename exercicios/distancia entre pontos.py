import math

x1 = float(input('digite o valor de x1  '))
y1 = float(input('digite o valor de y1  '))
x2 = float(input('digite o valor de x2  '))
y2 = float(input('digite o valor de y2  '))

p1 = (x1, y1)
p2 = (x2, y2)

D = ((x1 - x2) ** 2) + ((y1 - y2) ** 2)

result = math.sqrt(D)

if result >= 10:
    print('longe')
else:
    print('perto')
