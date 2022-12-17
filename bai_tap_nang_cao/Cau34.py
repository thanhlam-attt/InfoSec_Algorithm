"""Cài đặt thuật toán kiểm tra số nguyên tố Fermat. Trong trường hợp nào thì số nào thì thuật toán cho kết quả kiểm
tra sai.
a ^ (n - 1) mod n = 1 với mọi a
Trường hợp kiểm tra sai: khi xuất hiện a sao cho n là hợp số nhưng vẫn có giá trị a thỏa mãn a ^ (n - 1) mod n = 1
ví dụ 341 = 11 * 31 mà 2^340 mod 341 = 1, a gọi là giá trị đánh lừa
"""
import random


def GCD(a, b):
    if a % b == 0:
        return b
    return GCD(b, a % b)


def phantich_nhiphan(num):
    binary = []
    while num != 0:
        sodu = num % 2
        num = num // 2
        binary.append(sodu)
    binary.reverse()
    return binary


def nhanbinhphuong_colap(num_a, num_k, num_n):
    K = phantich_nhiphan(num_n)
    K.reverse()
    A = num_a
    if K[0] == 0:
        b = 1
    else:
        b = num_a
    for i in range(len(K)):
        A = (A ** 2) % num_n
        if K[i] == 1:
            b = (b * A) % num_n
    return b


def fermat_prime(num, t):
    for i in range(1, t + 1):
        a = random.randint(2, num - 1)
        if nhanbinhphuong_colap(a, num - 1, num) != 1:
            return False
    return True


if __name__ == '__main__':
    num_n = int(input("Nhập n: "))
    num_t = int(input("Nhập tham số an toàn: "))
    if fermat_prime(num_n, num_t):
        print(f"{num_n} là số nguyên tố!")
    else:
        print(f"{num_n} là số hợp số!")
