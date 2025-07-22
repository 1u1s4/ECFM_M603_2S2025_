n = 3

def es_palindromo(x):
    x = str(x)
    return x == x[::-1]

def main():
    soluciones = []
    for x in range(10**n-1, 99, -1):
        for y in range(10**n-1, 99, -1):
            if es_palindromo(x*y):
                soluciones.append((x*y, x, y))

    print(max(soluciones))

main()