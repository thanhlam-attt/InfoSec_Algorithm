"""Tìm nghịch đảo của một số a trong trường F_p với a và p được nhập từ bàn phím."""


def GCD(num_a, num_b):
    if num_a % num_b == 0:
        return num_b
    return GCD(num_b, num_a % num_b)


def EuclideExtend(a, p):
    if GCD(a, p) != 1:
        return -1
    y2 = 0
    y1 = 1
    while p > 0:
        q = a // p
        r = a % p
        y = y2 - y1 * q
        a = p
        p = r
        y2 = y1
        y1 = y
    while y2 < 0:
        y2 += a
    return y2


if __name__ == '__main__':
    num_a = int(input("Nhập a: "))
    num_p = int(input(f"Nhập p > {num_a}: "))
    while num_p < num_a:
        num_p = int(input(f"Nhập lại p > {num_a}: "))
    NghichDao = EuclideExtend(num_p, num_a)
    if NghichDao != -1:
        print(f"Nghịch đảo của {num_a} mod {num_p} là: {NghichDao}")
    else:
        print(f"Không tồn tại nghịch đảo của {num_a} mod {num_p}")
