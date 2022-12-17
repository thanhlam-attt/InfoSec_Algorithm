"""Viết chương trình tìm các số Carmichael (là các số giả nguyên tố n thoả mãn điều kiện là hợp số và thoả mãn b^(
n-1)≡1 (mod n) với mọi số nguyên dương b nguyên tố cùng nhau với n) nhỏ hơn một số N cho trước nhập vào từ bàn phím (
với điều kiện 0≤N≤10000. """
import math
import time


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


def GCD(num_a, num_b):
    if num_a % num_b == 0:
        return num_b
    return GCD(num_b, num_a % num_b)


def modpower(a, b, p):
    if b == 1:
        return a
    elif b == 0:
        return 1
    else:
        x = modpower(a, math.floor(b / 2), p)
        if b % 2 == 0:
            return (x * x) % p
        else:
            return (x * x * a) % p


def is_carmi(num_n):
    if check_prime(num_n):
        return False
    else:
        for b in range(2, num_n):
            if GCD(num_n, b) == 1:
                if modpower(b, num_n - 1, num_n) != 1:
                    return False
    return True


after = time.time()
if __name__ == '__main__':
    num = int(input("Nhập N > 0: "))
    while num < 0:
        num = int(input("Nhập N > 0: "))

    for i in range(2, num + 1):  # 0 và 1 không phải số Carmichael vì 0 và 1 không phải số nt cũng kp hợp số
        if is_carmi(i):
            print(i, " ", end='')
    elapsed = time.time() - after
    print(f"\nThời gian thực hiện thuật toán là {elapsed}")