""" Áp dụng các thuật toán đã được học em hãy cài đặt chương trình giải bài toán mô phỏng cách mã và giải mã của hệ mật
RSA như sau:
-	Tìm số nguyên số p, q (trong đó 100 < p, q < 500)
-	Tính n = p.q; (n) = (p – 1) (q – 1)
-	Chọn e là số nguyên tố cùng nhau với (n) (gcd(e, (n)) = 1) và tính d = e^(-1) mod (n)
-	Tính bản mã c của thông điệp m, với m = SBD + 123, c = m^e mod n
-	Giải mã thông điệp, tính m = c^d mod n
"""
import math
import random


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


def GCD(a, b):
    if a % b == 0:
        return b
    return GCD(b, a % b)


def Tinh_Modulo_So_Mu_Lon(a, k, num):
    K = []
    while k != 0:
        du = k % 2
        k = k // 2
        K.append(du)
    A = a
    if K[0] == 0:
        b = 1
    else:
        b = a
    for i in range(1, len(K)):
        A = (A ** 2) % num
        if K[i] == 1:
            b = (A * b) % num
    return b


def EuclideExtend(a, b):
    y2 = 0
    y1 = 1
    A = a
    while b != 0:
        q = a // b
        r = a % b
        y = y2 - y1 * q
        a = b
        b = r
        y2 = y1
        y1 = y
    while y2 < 0:
        y2 += A  # nếu để là a như cũ thì sau vòng lặp while trên a sẽ về 1 => đáp án sai
    return y2


def randomP():
    while True:
        p = random.randint(100, 500)
        if check_prime(p):
            return p


def randomE(phi_num):
    while True:
        num_e = random.randint(2, phi_n)
        if GCD(num_e, phi_num) == 1:
            return num_e


if __name__ == '__main__':
    q = randomP()
    p = randomP()
    n = q * p
    phi_n = (p - 1) * (q - 1)
    e = randomE(phi_n)
    d = EuclideExtend(phi_n, e)

    sbd = int(input("Nhập số báo danh: "))
    sbd = sbd + 123

    print("======================================")
    print(f"Thông tin thành phần:\n p = {p}, q = {q}, n = {n}\n phi_n = {phi_n}, e = {e}, d = {d}")

    print("======================================")
    cypher = Tinh_Modulo_So_Mu_Lon(sbd, e, n)
    print(f"Bản mã của {sbd} là: {cypher}")

    text = Tinh_Modulo_So_Mu_Lon(cypher, d, n)
    print(f"Bản rõ của {cypher} là: {text}")
