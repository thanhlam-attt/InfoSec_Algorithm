import math


def ln(x):
    if x <= 0:
        return -1
    if x == 1:
        return 0
    k = 100
    r = 0
    for i in range(k + 1):
        r += 2 * math.pow((x - 1) / (x + 1), 2 * i + 1) / (2 * i + 1)
    return r


def a_mux(a, x):
    if x == 1:
        return a
    if x == 0:
        return 1
    else:
        return 2.71828 ** (x * ln(a))


if __name__ == '__main__':
    a = float(input("Nhập a: "))
    x = float(input("Nhập x: "))
    print(f"a^x = {a_mux(a, x)}")
