# hàm tính a^b (với b kiểu số nguyên dương thôi)
def pow(a, b):
    r = 1
    for i in range(b):
        r *= a
    return r


# hàm tính ln(x)
def ln(x):
    if x <= 0:
        return -1
    # x>0
    # chọn luôn k = 100
    k = 100
    r = 0
    for i in range(k + 1):
        r += 2 * pow((x - 1) / (x + 1), 2 * i + 1) / (2 * i + 1)
    return r


# hàm tính log(base, b)
def log(base, b):
    if base == 1 or base <= 0 or b <= 0:
        return -1
    return ln(b) / ln(base)


# main
print(log(-2, 9))
print(log(11, 90))
print(log(2, 80))