""" Cài đặt thuật toán kiểm tra số nguyên tố Miller-Rabin 
in ra kết luận về 1 số nguyên dương N nhập vào từ bàn phím với xác suất kết luận tương ứng sau thuật toán. """
import random

"""
n - 1 = 2^s.r với r lẻ 
    n lẻ => n-1 chia 2, s = 1, r = n, lặp lại nếu chia hết cho 2 => tăng biến s lên 1 đơn vị, r = r // 2 
            tới khi không chia được cho 2 nữa => return (s, r)
for i = 1 to t do:
    random a, 2 <= a <= n-2
    tính y = a^r mod n
    Nếu y != 1 và y != n-1:
        j = 1
        while j <= s - 1 and y != n - 1 do:
            tính y = y^2 mod n
            if y == 1 return "hợp số"
            j += 1
        y != n - 1 return "hợp số"
return "Nguyên tố"
"""


def Modulo(num_a, num_k, num_n):  # Sử dụng nhân bình phương có lặp
    K = []
    while num_k > 0:
        r = num_k % 2
        num_k = num_k // 2
        K.append(r)
    A = num_a
    if K[0] == 0:
        b = 1
    else:
        b = num_a
    for i in range(1, len(K)):
        A = (A ** 2) % num_n
        if K[i] == 1:
            b = (b * A) % num_n
    return b


def Miller_rabin(n, t):
    # if n == 3:
    #     return "Nguyên tố"
    # if n % 2 == 0:
    #     return "Hợp số"
    # Phân tích n-1 = 2^s.r
    s = 0
    r = n - 1
    while r % 2 == 0:
        s += 1
        r = r // 2
    # Vòng for
    for i in range(t):
        a = random.randint(2, n - 2)
        y = Modulo(a, r, n)
        if y != 1 and y != n - 1:
            j = 1
            while j <= s - 1 and y != n - 1:
                y = (y ** 2) % n  # vì ở thuật toán có ghi là số ngto nếu a ^ (2^j*r) mod n = 1
                if y == 1:
                    return "Hợp số"
                j += 1
            if y != n - 1:
                return "Hợp số"
    return "Nguyên tố"


if __name__ == '__main__':
    n = int(input("Nhập n >= 3: "))
    while n < 3:
        n = int(input("Nhập lại n >= 3: "))
    t = int(input("Nhập t >= 1: "))
    while t < 1:
        t = int(input("Nhập lại t >= 1: "))
    print(n, "là: " + Miller_rabin(n, t))
    print("Xác suất kết luận: ", 1 - ((1 / 4) ** t))
