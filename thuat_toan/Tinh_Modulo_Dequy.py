import math


# a^b = (a^(b/2))^2 nếu b chẵn
# a^b = a*(a^(b/2))^2 nếu b lẻ
# a^b = a nếu b = 1

def modpower(a, b, p):
    if b == 1:
        return a
    elif b == 0:
        return 1
    else:
        x = modpower(a, math.floor(b / 2), p)
        if b % 2 == 0:
            return (x * x) % p
        else:
            return (x * x * a) % p


if __name__ == '__main__':
    a = int(input("Nhập a: "))
    b = int(input("Nhập b: "))
    p = int(input("Nhập p: "))

    print(modpower(a, b, p))
