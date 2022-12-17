def SangNT(a, b):
    prime = [True for i in range(1, b + 1)]
    prime[0] = False
    prime[1] = False
    for i in range(2, b):
        if prime[i]:
            for j in range(i * 2, b, i):  # 2*i, 3*i, 4*i, ... => step = i
                prime[j] = False

    for p in range(a, b):
        if prime[p]:
            print(p, " ", end='')


if __name__ == '__main__':
    so_a = int(input("Nhập a: "))
    so_b = int(input("Nhập b: "))
    if so_a > so_b:
        temp = so_a
        so_a = so_b
        so_b = temp
    SangNT(so_a, so_b)
