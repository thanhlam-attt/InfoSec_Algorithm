"""Với một số nguyên dương N thoả mãn 0<N<10000, đặt:
F ( N ) = N nếu N là một số nguyên tố
F ( N ) = 0 nếu là hợp số
Cho  L và R nhập vào từ bàn phím, với mọi cặp i , j trong khoảng [ L , R ] hãy viết chương trình in ra màn hình
giá trị của tổng F ( i ) * F ( j ) với  j > i.
"""
""" Về bản chất thì là tính tổng tích đề các của tập số nguyên tố trong khoảng L, R"""
import math


def check_prime(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    else:
        for loop in range(2, int(math.sqrt(num)) + 1):
            if num % loop == 0:
                return False
        return True


def result_func(num_a, num_b):
    result = 0
    for i in range(num_a, num_b + 1):
        if check_prime(i):
            for j in range(i + 1, num_b + 1):
                if check_prime(j):
                    result += i * j
    return result


if __name__ == '__main__':
    num_l = int(input("Nhập L: "))
    num_r = int(input(f"Nhập R > {num_l}: "))
    while num_r < num_l:
        num_r = int(input(f"Nhập lại R > {num_l}: "))

    print(result_func(num_l, num_r))
