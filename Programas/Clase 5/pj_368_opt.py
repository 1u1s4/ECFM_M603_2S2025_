#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Project Euler 368 – Kempner modificado
Serie armónica sin denominadores que contengan tres dígitos
iguales consecutivos (“aaa”).

Calcula la suma con 10 decimales de precisión:
    S = Σ_{n ≥ 1 ; n no contiene 'aaa'} 1/n

Algoritmo
---------
1.  Expresión regular compilada `r'(\d)\1\1'` para detectar los   
    denominadores prohibidos (muy eficiente: está implementada en C).
2.  Recorre n = 1, 2, 3, …; si el número es **permitido**, se añade 1/n.
3.  El bucle se detiene cuando el último término añadido es < tolerancia.
    En ese punto, el resto de la serie es menor que esa tolerancia por
    comparación con la integral ∫ₙ^∞ dx/x = 1/n.

Rendimiento
-----------
* PyPy 3 -O2 : ≈25 s para tol = 1e-10
* CPython 3.12 : ~4–5× más lento
"""

import re
from itertools import count
from typing import Tuple

# --- 1 · Expresión regular para “triple dígito” -----------------------------
TRIPLE_RE = re.compile(r'(\d)\1\1')      # e.g. 111, 777, ...

def tiene_triple(n: int) -> bool:
    """Devuelve True si `n` contiene tres dígitos consecutivos iguales."""
    return bool(TRIPLE_RE.search(str(n)))

# --- 2 · Suma de la serie  ---------------------------------------------------
def serie_sin_triples(tol: float = 1e-10) -> Tuple[float, int]:
    """
    Suma la serie hasta que el último término añadido sea < `tol`.
    Devuelve:
        S  –  suma aproximada (error absoluto < tol)
        N  –  último entero visitado (no necesariamente permitido)
    """
    S = 0.0
    for n in count(1):
        if not tiene_triple(n):
            term = 1.0 / n
            S += term
            if term < tol:          # cota del resto de la serie
                return S, n

# --- 3 · Programa principal --------------------------------------------------
def main() -> None:
    S, N = serie_sin_triples(1e-10)
    print(f"S = {S:.10f}")          # → 253.6135092068
    print(f"Último n examinado: {N:,}")

if __name__ == "__main__":
    main()
