"""Áp dụng theo các thuật toán đã được học trong phần lí thuyết em hãy cài đặt chương trình:
-	Tìm số nguyên tố k gần nhất với phần số của mã số sinh viên của mình (trong trường hợp khoảng cách bằng nhau thì lấy
số nhỏ hơn).
-	Từ số k tìm được tính ak mod n với a = SBD, n = 123456.
"""


def Eratos(num):
    prime = [True for i in range(num + 1)]
    prime[0] = prime[1] = False
    for i in range(2, num + 1):
        if prime[i]:
            for j in range(2 * i, num + 1, i):
                prime[j] = False
    return prime


def SoNhoHon(num):
    prime = Eratos(2000000)
    q = num
    while prime[q] is False:  # vì số nguyên tố là số lẻ trừ số 2 nên nếu q lẻ thì -2 còn q chẵn -1
        if q % 2 == 0:
            q -= 1
        else:
            q -= 2
    return q


def SoLonHon(num):
    prime = Eratos(2000000)
    p = num
    while prime[p] is False:
        if p % 2 == 0:
            p += 1
        else:
            p += 2
    return p


if __name__ == '__main__':
    num_n = int(input("Nhập mã số sinh viên > 0: "))
    while num_n < 0:
        num_n = int(input("Nhập lại mã số sinh viên phải > 0!: "))
    num_q = SoNhoHon(num_n)
    num_p = SoLonHon(num_n)
    if (num_n - num_q) == (num_n - num_p):
        print(f"Số nguyên tố gần nhất với {num_n} là: {num_q}")
    elif (num_n - num_q) > (num_n - num_p):
        print(f"Số nguyên tố gần nhất với {num_n} là: {num_p}")
    else:
        print(f"Số nguyên tố gần nhất với {num_n} là: {num_q}")
