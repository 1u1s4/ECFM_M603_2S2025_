"""
Problema 368 de P.E. que trata de ...
"""
import re

TRIPLE_RE = re.compile(r'(\d)\1\1')

def Qtermino(x: int) -> bool:
    """
    Permite determinar dado x un entero si es cumple que tiene
    3 o mas digitos iguales consecutivos.
    """
    x = str(x)
    n = len(x)
    for i in range(2, n):
        sub_x = x[i - 2: i + 1]
        for d in range(0, 10):
            if sub_x.count(str(d)) >= 3:
                return True
    return False

def _Qtermino(n: int) -> bool:
    return bool(TRIPLE_RE.search(str(n)))

def solve() -> float:
    y_n = []
    x_n = []
    contador = 0
    indice_yn = 1
    error = 1
    TOL = 10**-10
    while contador < 10**6:
        while True:
            if Qtermino(indice_yn):
                y_n.append(indice_yn)
                indice_yn += 1
                break
            else:
                indice_yn += 1
        
        if contador == 0:
            x_nuevo = 0
            for k in range(1, y_n[0] + 1):
                x_nuevo += 1 / k
            x_nuevo -= 1 / y_n[0]
            x_n.append(x_nuevo)
        else:
            x_nuevo = x_n[contador - 1]
            i = y_n[contador - 1] + 1
            j = y_n[contador]
            for k in range(i, j + 1):
                x_nuevo += 1 / k
            x_nuevo -= 1 / y_n[contador]
            x_n.append(x_nuevo)
            if j > i:
                error = abs(x_n[contador] - x_n[contador - 1])
        contador += 1
    return x_n[-1]

import time
start_time = time.time()
print(solve())
print("Tiempo de ejecucion:", time.time() - start_time)
# 253.6135092068