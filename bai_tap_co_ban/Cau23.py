"""Viết chương trình in ra màn hình YES trong trường hợp tổng của các số nguyên tố trong khoảng [A, B] là cũng là một
số nguyên tố và NO nếu ngược lại. Với A,B là hai số được nhập vào từ bàn phím """

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


def sum_eratos(num_a, num_b):
    prime = [True for i in range(0, num_b + 1)]
    prime[0] = prime[1] = False
    for i in range(2, num_b + 1):
        if prime[i]:
            for j in range(i * 2, num_b + 1, i):
                prime[j] = False
    result = 0
    for i in range(num_a, num_b + 1):
        if prime[i]:
            result += i
    if check_prime(result):
        return True
    else:
        return False


if __name__ == '__main__':
    num_A = int(input("Nhập A: "))
    num_B = int(input(f"Nhập B > {num_A}: "))
    while num_B < num_A:
        num_B = int(input(f"Nhập lại B > {num_A}: "))

    if sum_eratos(num_A, num_B):
        print("YES")
    else:
        print("NO")
