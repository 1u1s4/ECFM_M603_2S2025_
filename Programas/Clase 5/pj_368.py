
def Qtermino(x: int) -> bool:
    x = str(x)
    n = len(x)
    for i in range(2, n):
        sub_x = x[i - 2: i + 1]
        for d in range(0, 10):
            if sub_x.count(str(d)) >= 3:
                return True
    return False

for i in range(10**100):
    if Qtermino(i):
        print(i)