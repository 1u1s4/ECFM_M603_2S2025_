
def convert(n: int, b: int) -> list[int]:
    '''
    Devuelve la cadena de digitos de la 
    representación de n en base b
    '''
    digitos = []
    cociente = n
    while cociente > 0:
        residuo = cociente%b
        cociente = cociente // b

        digitos.append(residuo)


    return digitos[::-1]

print(convert(10001**19, 2))