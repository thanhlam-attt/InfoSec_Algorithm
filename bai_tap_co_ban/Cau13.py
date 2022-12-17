""" Viết chương trình tìm hai số nguyên tố nhỏ hơn hoặc bằng N với N nhập vào từ bàn phím,
sao cho tổng và hiệu của chúng đều là số nguyên tố.
"""
"""
a - b = c và a + b = d => a = c + b và a = d - b => c + b = d - b 
mà b, c, d đều là số nguyên tố nên để c + b và d - b lẻ thì b chẵn => b = 2
Bài toán đưa về dạng tìm a sao cho a - 2 và a + 2 cùng là số nguyên tố
"""
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


def check_2prime(num_a):
    if check_prime(num_a) and check_prime(num_a + 2) and check_prime(num_a - 2):
        return True
    return False


if __name__ == '__main__':
    num_n = int(input("Nhập N: "))
    for i in range(1, num_n + 1):
        if check_2prime(i):
            print(2, " - ", i)
