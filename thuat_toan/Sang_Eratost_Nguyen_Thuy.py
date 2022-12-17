def SangNT(n):
    prime = [True for i in range(1, n + 1)]
    prime[0] = False
    prime[1] = False
    for i in range(2, n):
        if prime[i]:
            for j in range(i * 2, n, i):  # 2*i, 3*i, 4*i, ... => step = i
                prime[j] = False
    for p in range(0, n):
        if prime[p]:
            print(p, " ", end='')


if __name__ == '__main__':
    so = int(input("Nhập n: "))
    SangNT(so)
