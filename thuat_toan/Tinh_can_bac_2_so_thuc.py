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


def sqrt_num(num):
    can_so = math.pow(2.71828, ln(num) / 2)
    return can_so


if __name__ == '__main__':
    num_n = float(input("Nhập n: "))
    print(f"Căn của {num_n} là:", sqrt_num(num_n))
