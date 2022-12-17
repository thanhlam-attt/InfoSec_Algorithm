""" Viết chương trình Hai số nguyên tố sinh đôi là hai số nguyên tố hơn kém nhau 2 đơn vị.
Tìm hai số nguyên tố sinh đôi nhỏ hơn hoặc bằng N, với N được nhập vào từ bàn phím."""
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


def check_2prime(num):
    if check_prime(num) and check_prime(num + 2):
        return True
    return False


if __name__ == '__main__':
    num_n = int(input("Nhập N: "))
    for i in range(2, num_n):
        if check_2prime(i):
            print(i, " - ", i + 2)