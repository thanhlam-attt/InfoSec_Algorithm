"""Cho mảng A nhập từ bàn phím gồm các số nguyên dương. Hãy viết chương trình đếm các cặp số (i,j) trong mảng A sao
cho ước chung lớn nhất của chúng là một số nguyên tố. """

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


def GCD(a, b):
    if a % b == 0:
        return b
    return GCD(b, a % b)


if __name__ == '__main__':
    list_A = []
    num_n = int(input("Nhập số phần tử của mảng > 0: "))
    while num_n < 0:
        num_n = int(input("Nhập lại số phần tử của mảng > 0: "))

    for i in range(num_n):
        list_A.append(int(input(f"Nhập phần tử A[{i}]: ")))

    count = 0
    for i in range(num_n):
        for j in range(i + 1, num_n):
            if check_prime(GCD(list_A[i], list_A[j])):
                count += 1
    print(f"số các cặp số (i,j) trong mảng A thỏa mãn là: {count}")
