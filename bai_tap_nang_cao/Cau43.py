"""Cho N nhập vào từ bàn phím (0<N<1000), hãy viết chương trình tìm tất cả các số nguyên a<N sao cho a^p mod N là số
nguyên tố. """
import random


def eratos(num):
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


def sinhso_ngto():
    prime = eratos(1000)
    num = random.randint(1, 1000)
    while prime[num] is False:
        num = random.randint(1, 1000)
    return num


if __name__ == '__main__':
    num_n = int(input("Nhập n (0<N<1000): "))
    while num_n < 0 or num_n > 1000:
        num_n = int(input("Nhập lại n (0<N<1000): "))
    prime = eratos(num_n)
    p = sinhso_ngto()
    print(f"p = {p}")
    for a in range(2, num_n):
        if prime[tinh_mod(a, p, num_n)]:
            print(a, " ", end='')

