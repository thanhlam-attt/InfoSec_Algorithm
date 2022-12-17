""" Viết chương trình tính tổng của các số nguyên tố nằm trong khoảng [A, B] với A, B nhập vào từ bàn phím."""


def SangNT(a, b):
    prime = [True for i in range(1, b + 1)]
    prime[0] = False
    prime[1] = False
    for i in range(2, b):
        if prime[i]:
            for j in range(i * 2, b, i):  # 2*i, 3*i, 4*i, ... => step = i
                prime[j] = False
    cout = 0
    for p in range(a, b):
        if prime[p]:
            cout += p
    return cout


if __name__ == '__main__':
    num_a = int(input("Nhập A: "))
    num_b = int(input(f"Nhập B > {num_a}: "))
    while num_b < num_a:
        num_b = int(input(f"Nhập lại B > {num_a}: "))

    print(SangNT(num_a, num_b))
