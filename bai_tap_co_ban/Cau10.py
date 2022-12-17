""" Viết chương trình đếm số ước và số ước nguyên tố của một số N nhập vào từ bàn phím."""
import math


def CheckPrime(number_check):
    if number_check < 2:
        return 0
    elif number_check == 2:
        return 1
    else:
        for loop in range(2, int(math.sqrt(number_check)) + 1):
            if number_check % loop == 0:
                return 0
        return 1


def TinhUoc_N(number):
    k = 0
    s = 0
    for i in range(1, number + 1):
        if number % i == 0:
            s += 1
            if CheckPrime(i) == 1:
                print(i, " ", end="")
                k += 1
    print("Số ước là : ", s, "Số ước nguyên tố là: ", k)


if __name__ == '__main__':
    num = int(input("Nhập n: "))
    TinhUoc_N(num)

