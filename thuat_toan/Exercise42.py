'''
Câu 42. Viết chương trình sinh ra 2 số nguyên tố 0<p,q<1000 và kiểm tra với với số 0<a<100 thì
liệt kê những số a thoả mãn: a^p mod q là số nguyên tố.
'''
import math
import random


def is_prime(n):
    if n < 2:
        return False
    for x in range(2, int(math.sqrt(n) + 1)):
        if n % x == 0:
            return False
    return True


def random_number():
    while True:
        num = random.randint(2, 1000)
        if is_prime(num):
            return num


def square_integer(number_a, number_k, number_n):
    k = []
    while number_k > 0:
        k.append(int(number_k % 2))
        number_k = int(number_k // 2)
    a = number_a
    if k[0] == 1:
        b = a
    else:
        b = 0
    for i in range(1, len(k)):
        a = (a * a) % number_n
        if k[i] == 1:
            b = (b * a) % number_n
    return b


p = random_number()
q = random_number()
print(p)
print(q)
for a in range(2, 100):
    b = square_integer(a, p, q)
    if is_prime(b):
        print(f'{a}:{b} ', end=" ")
