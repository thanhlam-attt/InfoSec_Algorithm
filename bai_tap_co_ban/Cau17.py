""" Viết chương trình tìm số nguyên dương x nhỏ nhất sao cho giá trị của biểu thức Ax^2+Bx+C là một số nguyên tố
với A,B,C là các số nguyên nhập vào từ bàn phím. """
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
    num_n = int(input("Nhập vùng kiểm tra 0 -> n: "))
    num_a = int(input("Nhập giá trị A: "))
    num_b = int(input("Nhập giá trị B: "))
    num_c = int(input("Nhập giá trị C: "))
    check = 0
    if check_prime(num_c):
        print("Giá trị nhỏ nhất là:", 0, " - Giá trị của biểu thức tại x =", 0, "là:", num_c)
        check = 1
    elif check_prime(num_a + num_b + num_c):
        print("Giá trị nhỏ nhất là:", 1, " - Giá trị của biểu thức tại x =", 1, "là:", num_a + num_b + num_c)
        check = 1
    else:
        for num_x in range(0, num_n):
            val = num_a * (num_x ** 2) + num_b * num_x + num_c
            if check_prime(val):
                check = 1
                print("Giá trị nhỏ nhất là:", num_x, " - Giá trị của biểu thức tại x =", num_x, "là:", val)
                break
    if check == 0:
        print("Không có giá trị thỏa mãn!")
