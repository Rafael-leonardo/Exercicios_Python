def binario():
    codigo = input('Escreva o codigo binario:  ')
    b = len(codigo)
    contador = b-1
    d = 0

    if b > 8:
        print('Ops! Só é permitido codigos até 8 digitos.')
    else:
        for num in codigo:
            c = int(num)*(2**contador)
            contador -= 1
            d += c
        print(f'O resultado do codigo binário {codigo}, é equivalente a {d}.')
        print(f'Caso o codigo {codigo}, contenha valores diferentes de 0 e 1 \no resultado pode estar errado.')

binario()
