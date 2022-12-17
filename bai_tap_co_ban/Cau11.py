""" Viết chương trình tính tổng của các số nguyên tố nhỏ hơn hoặc bằng N với N được nhập từ bàn phím. """


def SangNT(b):
    prime = [True for i in range(1, b + 1)]
    prime[0] = False
    prime[1] = False
    for i in range(2, b):
        if prime[i]:
            for j in range(i * 2, b, i):  # 2*i, 3*i, 4*i, ... => step = i
                prime[j] = False
    cout = 0
    for p in range(2, b):
        if prime[p]:
            cout += p
    return cout


if __name__ == '__main__':
    so_n = int(input("Nhập n: "))
    print(SangNT(so_n))
