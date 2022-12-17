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
import random


def trans_binary(num):
    binary = []
    while num > 0:
        r = num % 2
        num = num // 2
        binary.append(r)
    binary.reverse()
    return binary


def Modulo(num_a, num_k, num_n):  # Sử dụng nhân bình phương có lặp
    K = trans_binary(num_k)
    K.reverse()
    A = num_a
    if K[0] == 0:
        b = 1
    else:
        b = num_a
    for i in range(1, len(K)):
        A = (A ** 2) % num_n
        if K[i] != 0:
            b = (b * A) % num_n
    return b


def Miller_rabin(n, t):
    # Phân tích n-1 = 2^s.r
    s = 0
    r = n - 1
    while r % 2 == 0:
        s += 1
        r = r // 2

    # Vòng for
    for i in range(1, t + 1):
        a = random.randint(2, n - 1)  # Không chọn a = 1 vì khi đó y luôn luôn bằng 1,
        # không chọn a = n - 1 vì a ^ (n - 1) mod n khi đó y luôn = 1
        y = Modulo(a, r, n)
    if y != 1 and y != n - 1:
        j = 1
        while j <= s - 1 and y != n - 1:
            y = Modulo(y, 2, n)  # tính y = y^2 mod n
            if y == 1:  # if y == 1 return "hợp số"
                return "Hợp số"
            j += 1  # j += 1
        if y != n - 1:
            return "Hợp số"  # y != n - 1 return "hợp số"
    return "Nguyên tố"


if __name__ == '__main__':
    n = int(input("Nhập n: "))
    t = int(input("Nhập t: "))
    print(n, "là: " + Miller_rabin(n, t))
