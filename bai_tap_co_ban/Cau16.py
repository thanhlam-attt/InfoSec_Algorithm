""" Viết chương trình tìm các số nguyên tố từ một mảng sinh ngẫu nhiên có kích thước N, với N nhập vào từ bàn phím """
import math

from numpy import random


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


if __name__ == '__main__':
    num_n = int(input("Nhập kích thước mảng: "))
    num_a = int(input("Nhập vùng random 0 - n: "))
    list_random = random.randint(num_a, size=num_n)
    print("Mảng sinh là: ")
    print(list_random)
    print("\nCác phần tử nguyên số trong mảng là: ")
    for i in range(0, len(list_random)):
        if check_prime(list_random[i]):
            print(list_random[i], " ", end='')
