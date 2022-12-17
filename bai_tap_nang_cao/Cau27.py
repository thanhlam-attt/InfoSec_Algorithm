"""Viết chương trình in ra các cặp số (a,b) thoả mãn điều kiện 0<a,b<1000, sao cho ước chung lớn nhất của 2 số đó là
một số nguyên tố. """
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
    i = 0
    for num_a in range(1000):
        for num_b in range(num_a + 1, 1000):
            if check_prime(GCD(num_a, num_b)):
                print(num_a, " - ", num_b, f"GCD({num_a}, {num_b}) = ", GCD(num_a, num_b))
                i += 1
    print(i)
