from math import isqrt

def exponent_in_factorial(m, p):
    """v_p(m!)"""
    total = 0
    while m:
        m //= p
        total += m
    return total

def min_m_for_p_power(p, a):
    """m_{p,a} usando búsqueda binaria"""
    lo, hi = 1, p * a          # cota superior inicial (bastante holgada)
    while exponent_in_factorial(hi, p) < a:
        hi *= 2                # garantiza que la cota superior sirva
    while lo < hi:
        mid = (lo + hi) // 2
        if exponent_in_factorial(mid, p) >= a:
            hi = mid
        else:
            lo = mid + 1
    return lo

def factoriza(n):
    """factores primos: {p: a} (trial division sencillo)"""
    fac, d = {}, 2
    while d * d <= n:
        while n % d == 0:
            fac[d] = fac.get(d, 0) + 1
            n //= d
        d += 1 if d == 2 else 2   # 2, 3, 5, 7…
    if n > 1:
        fac[n] = fac.get(n, 0) + 1
    return fac

def s(n):
    if n == 1:
        return 1
    return max(min_m_for_p_power(p, a) for p, a in factoriza(n).items())

def S(N):
    return sum(s(i) for i in range(2, N + 1))

print(S(100))