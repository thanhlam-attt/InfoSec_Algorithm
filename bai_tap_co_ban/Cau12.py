"""Viết chương trình tìm bốn số nguyên tố liên tiếp, sao cho tổng của chúng là số nguyên tố nhỏ hơn hoặc bằng N
(với N được nhập vào từ bàn phím)."""
import math

"""
a + b + c + d = e
e là số nto > 2 => e là số lẻ
b, c, d là số ngto > 2 => b, c, d lẻ => b + c + d lẻ
để e lẻ => a phải là snt chẵn => a = 2 
"""


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


if __name__ == '__main__':
    num_n = int(input("Nhập N: "))
    prime = [i for i in range(1, num_n) if check_prime(i)]
    for i in range(len(prime) - 4):
        if check_prime(prime[i] + prime[i + 1] + prime[i + 2] + prime[i + 3]):
            print(prime[i], " ", prime[i + 1], " ", prime[i + 2], " ", prime[i + 3])
