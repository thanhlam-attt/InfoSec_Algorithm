""" Cho một số nguyên dương N, gọi:
k là số ước nguyên tố của N;
q là tổng của các ước nguyên tố của N;
p là tổng của các ước số của N;
s là số ước của N;
Hãy viết chương trình tính giá trị của: N+p+s-q-k với N cho trước nhập từ bàn phím.
Ví dụ: N=24, có các ước là {1,2,3,4,6,8,12, 24} do đó: 
p=1+2+3+4+6+8+12+24=60 và s=8
trong đó có 2 ước nguyên tố là {2,3} do đó:
q=2+3=5 và k=2
Và từ đó: N+p+s-q-k = 24+60+8-5-2=85;
"""
import math


def CheckPrime(number_check):
    if number_check < 2:
        return 0
    else:
        for loop in range(2, int(math.sqrt(number_check)) + 1):
            if number_check % loop == 0:
                return 0
        return 1


def Sum_N(n):
    k = 0
    q = 0
    p = 0
    s = 0
    for i in range(1, n + 1):
        if n % i == 0:
            p += i
            s += 1
            if CheckPrime(i) == 1:
                print(i, " ", end="")
                k += 1
                q += i
    print(n, p, s, q, k)
    return n + p + s - q - k


if __name__ == '__main__':
    n = int(input("Nhập n: "))
    print("Giá trị cần tính là: ", Sum_N(n))
