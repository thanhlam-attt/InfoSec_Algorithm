"""Cho các số nguyên dương a,k,n, nhập từ bàn phím (0<a,k<n<1000), Viết chương trình xác định xem a^k mod n có phải là
một số nguyên tố hay không (sử dụng thuật toán bình phương và nhân có lặp)? """
import math


def check_prime(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True


def Binary(num):
    binary = []
    while num > 0:
        tail = num % 2
        num = num // 2
        binary.append(tail)
    binary.reverse()
    return binary


def NBP_CL(a, k, n):
    K = Binary(k)
    K.reverse()
    A = a
    if K[0] == 1:
        b = a
    else:
        b = 1
    for i in range(1, len(K)):
        A = (A ** 2) % n
        if K[i] != 0:
            b = (A * b) % n
    return b


if __name__ == '__main__':
    num_a = int(input("Nhập a > 0: "))
    while num_a < 0:
        num_a = int(input("Nhập lại a > 0: "))
    num_k = int(input("Nhập k > 0: "))
    while num_k < 0:
        num_k = int(input("Nhập lại k > 0: "))
    num_n = int(input("Nhập n > 0: "))
    while num_n < 0:
        num_n = int(input("Nhập lại n > 0: "))
    Value = NBP_CL(num_a, num_k, num_n)
    if check_prime(Value):
        print(f"{num_a}^{num_k} mod {num_n} = {Value} là số nguyên tố")
    else:
        print(f"{num_a}^{num_k} mod {num_n} = {Value} không là số nguyên tố")
