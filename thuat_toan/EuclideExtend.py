def GCD(a, b):
    if a % b == 0:
        return b
    return GCD(b, a % b)


def EuclideExtend(a, b):
    x2 = 1
    x1 = 0
    y2 = 0
    y1 = 1
    A = a
    while b > 0:
        q = a // b
        r = a % b
        x = x2 - q * x1
        y = y2 - q * y1
        a = b
        b = r
        x2 = x1
        x1 = x
        y2 = y1
        y1 = y
    while y2 < 0:
        y2 += A
        print(y2, " ", A)
    return y2


a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
if GCD(a, b) != 1:
    print("Không có nghịch đảo của", b, "mod", a, " !")
else:
    if a > b:
        print(b, "mode", a, "là: ", EuclideExtend(a, b))
    else:
        temp = a
        a = b
        b = temp
        print(b, "mode", a, "là: ", EuclideExtend(a, b))
