def maximo(v1, v2, v3):
    if v1 >= v2 and v1 >= v3:
        return print(f'o numero maior é {v1}. Entre {v1}, {v2} e {v3}.')
    if v2 >= v1 and v2 >= v3:
        return print(f'o numero maior é {v2}. Entre {v1}, {v2} e {v3}.')
    if v3 >= v1 and v3 >= v2:
        return print(f'o numero maior é {v3}. Entre {v1}, {v2} e {v3}.')

num1 = int(input('digite o primeiro numero da comparação: '))
num2 = int(input('digite o segundo numero da comparação: '))
num3 = int(input('digite o terceiro numero da comparação: '))

maximo(num1, num2, num3)