"""Phân tích n ra thừa số không tầm thường"""


# def Modulo(num_a, num_k, num_n):
#     if num_k == 0:
#         return 1
#     elif num_k == 1:
#         return num_a
#     else:
#         num_x = Modulo(num_a, num_k // 2, num_n)
#         if num_k % 2 == 0:
#             return num_x * num_x % num_n
#         else:
#             return num_x * num_x * num_a % num_n
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


def GCD(num_a, num_b):
    if num_a % num_b == 0:
        return num_b
    else:
        return GCD(num_b, num_a % num_b)


def Polla_Rho(num):
    a = 2
    b = 2
    while 1:
        a = Modulo(a ** 2 + 1, 1, num)
        b = Modulo(b ** 2 + 1, 1, num)
        b = Modulo(b ** 2 + 1, 1, num)
        d = GCD(abs(a - b), num)
        if 1 < d < num:
            return d
        elif d == num:
            print(f"Không tồn tại số thừa số không tầm thường của {num}")
            return -1


if __name__ == '__main__':
    num = int(input("Nhập số N > 0: "))
    while num < 0:
        num = int(input("Nhập lại N > 0: "))
    num_a = Polla_Rho(num)
    num_b = num // num_a
    print(f"{num} = {num_a} * {num_b}")
