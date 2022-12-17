"""Viết chương trình in ra các số nguyên dương nằm trong khoảng [m,l] sao cho giá trị của biểu thức Ax^2+Bx+C là một số nguyên tố.
Với A,B,C, m,l là các số nguyên nhập từ bàn phím (m<l)."""
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


if __name__ == '__main__':
    num_a = int(input("Nhập giá trị A: "))
    num_b = int(input("Nhập giá trị B: "))
    num_c = int(input("Nhập giá trị C: "))
    num_m = int(input("Nhập giá trị m: "))
    num_l = int(input("Nhập giá trị l: "))
    check = 0
    for num_x in range(num_m, num_l + 1):
        val = num_a * (num_x ** 2) + num_b * num_x + num_c
        if check_prime(val):
            check = 1
            print("Giá trị là:", num_x, " - Giá trị của biểu thức tại x =", num_x, "là:", val)
    if check == 0:
        print("Không có giá trị thỏa mãn trong khoảng này!")
