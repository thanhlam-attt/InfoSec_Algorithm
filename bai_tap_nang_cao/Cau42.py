"""Viết chương trình sinh ra 2 số nguyên tố 0<p,q<1000 và kiểm tra với với số 0<a<100 thì những số nào thoả mãn: a^p
mod q là số nguyên tố. """
import random


def Eratos(num):
    prime = [True for i in range(num + 1)]
    prime[0] = prime[1] = False
    for i in range(2, num + 1):
        if prime[i]:
            for j in range(2 * i, num + 1, i):
                prime[j] = False
    return prime


def tinh_mod(a, k, n):
    K = []
    while k > 0:
        r = k % 2
        k = k // 2
        K.append(r)
    A = a
    if K[0] == 0:
        b = 1
    else:
        b = a
    for i in range(1, len(K)):
        A = (A ** 2) % n
        if K[i] == 1:
            b = (A * b) % n
    return b


def sinhsoNT():
    prime = Eratos(1000)
    num = random.randint(1, 1000)
    while prime[num] is False:
        num = random.randint(1, 1000)
    return num


if __name__ == '__main__':
    p = sinhsoNT()
    q = sinhsoNT()
    prime = Eratos(q)  # vì a^p mod q không vượt quá q => chỉ cần Eratos(q)
    print(f"p = {p} và q = {q}")
    for a in range(100):
        if prime[tinh_mod(a, p, q)]:
            print(a, " ", end='')
