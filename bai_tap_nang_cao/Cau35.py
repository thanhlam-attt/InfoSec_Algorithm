""" Cài đặt thuật toán kiểm tra số nguyên tố Miller-Rabin 
in ra kết luận về 1 số nguyên dương N nhập vào từ bàn phím với xác suất kết luận tương ứng sau thuật toán. """
"""
n - 1 = 2^s.r với r lẻ 
    n lẻ => n-1 chia 2, s = 1, r = n, lặp lại nếu chia hết cho 2 => tăng biến s lên 1 đơn vị, r = r // 2 
            tới khi không chia được cho 2 nữa => return (s, r)
for i = 1 to t do:
    random a, 2 <= a <= n-2
    tính y = bai_tap_co_ban^r mod n
Nếu y != 1 và y != n-1:
    j = 1
    while j <= s - 1 and y != n - 1 do:
        tính y = y^2 mod n
        if y == 1 return "hợp số"
        j += 1
    y != n - 1 return "hợp số"
return "Nguyên tố"
"""


# def modpower(a, b, p):  # Tính bai_tap_co_ban^b mod p
#     if b == 1:
#         return a
#     elif b == 0:
#         return 1
#     else:
#         x = modpower(a, math.floor(b / 2), p)
#         if b % 2 == 0:
#             return (x * x) % p
#         else:
#             return (x * x * a) % p
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
        b = 0
    for i in range(len(K)):
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
        a = 5
        y = Modulo(a, r, n)
    if y != 1 and y != n - 1:
        j = 1
        while j <= s - 1 and y != n - 1:
            y = Modulo(y, 2, n)  # tính y = y^2 mod n
            if y == 1:  # if y == 1 return "hợp số"
                return "Hợp số"
            j += 1  # j += 1
        if y != n - 1: return "Hợp số"  # y != n - 1 return "hợp số"
    return "Nguyên tố"


if __name__ == '__main__':
    n = int(input("Nhập n: "))
    t = int(input("Nhập t: "))
    print(n, "là: " + Miller_rabin(n, t))
    print("Xác suất kết luận: ", 1 - ((1 / 4) ** t))
