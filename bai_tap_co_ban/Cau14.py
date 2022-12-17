"""Viết chương trình tìm số nguyên tố có ba chữ số, biết rằng nếu viết số đó theo thứ tự ngược lại thì ta được
một số là lập phương của một số tự nhiên."""
import math


def check_prime(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    else:
        for loop in range(2, int(math.sqrt(num)) + 1):
            if num % loop:
                return False
        return False


def check_cube(num):
    root_cube = num ** (1 / 3)
    if round(root_cube) ** 3 == num:
        return True
    else:
        return False


def reverse_num(num):
    rever_num = 0
    while num != 0:
        tail = num % 10
        rever_num = rever_num * 10 + tail
        num = num // 10
    return rever_num


def check_ReverseIsCube(num):
    if check_prime(num) and check_cube(reverse_num(num)):
        return True


if __name__ == '__main__':
    for i in range(10 ** (3 - 1), (10 ** 3)):
        if check_ReverseIsCube(i):
            print(i, " - ", reverse_num(i), " - ", reverse_num(i) ** (1/3))
