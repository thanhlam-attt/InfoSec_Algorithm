"""Một số gọi là siêu số nguyên tố nếu số lượng các số nguyên tố từ 1 đến X (ngoại trừ X) là một số nguyên tố.
Hãy viết chương trình đếm số lượng các siêu số nguyên tố này trong khoảng [A,B] cho trước nhập từ bàn phím."""
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


def Check_SuperPrime(num):
    if num == 1:  # num = 1 thì chỉ có sang_era[0] mà dưới có sét tới sang_era[1] => out of range => phải có đk riêng
        return False
    else:
        sang_era = [True for i in range(0, num)]
        sang_era[0] = False
        sang_era[1] = False
        for i in range(2, num):
            if sang_era[i]:
                for j in range(i * 2, num, i):
                    sang_era[j] = False
        count = 0
        for i in range(1, num):
            if sang_era[i]:
                count += 1
        if check_prime(count):
            return True
        else:
            return False


if __name__ == '__main__':
    num_a = int(input("Nhập A > 0: "))
    while num_a < 0:
        print("Nhập lại A!")
        num_a = int(input("Nhập A > 0: "))
    num_b = int(input(f"Nhập B > {num_a}: "))
    while num_b < num_a:
        print("Nhập lại B!")
        num_b = int(input(f"Nhập B > {num_a}: "))

    for loop in range(num_a, num_b + 1):
        if Check_SuperPrime(loop):
            print(loop, " ", end='')
