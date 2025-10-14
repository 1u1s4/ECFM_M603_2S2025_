
def collatz(n: int, contador: int = 1) -> int:
    if n == 1:
        return contador
    elif n % 2 == 0:
        return collatz(n // 2, contador + 1)
    else:
        return collatz(3 * n + 1, contador + 1)

"""
n_max = -1
longitud_max = -1
for n in range(1, 10**6 + 1):
    longitud_temp = collatz(n)
    if longitud_temp > longitud_max:
        longitud_max = longitud_temp
        n_max = n

print(n_max, longitud_max)}
"""
n_longitud = []
for n in range(1, 10**6 + 1):
    longitud_temp = collatz(n)
    n_longitud.append((longitud_temp, n))

print(max(n_longitud))