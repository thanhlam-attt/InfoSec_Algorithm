"""Lập trình tìm kiếm xâu S1 trong xâu S2 theo thuật toán Knutt-Morris-Patt. Trong trường hợp nào thì thuật toán
Boyer-Moore được xem là cải tiến hơn thuật toán tìm kiếm vét cạn? """


def failure(P):
    F = {}
    F[0] = -1
    F[1] = 0

    for i in range(2, len(P)):
        prefix = []
        suffix = []
        j = 1
        a = 1
        while j <= i:
            prefix.append(P[0:j])
            suffix.append(P[a:i])
            j += 1
            a += 1
        suffix.reverse()
        suffix.remove('')
        value = 0
        for x in range(i - 1):
            if prefix[x] == suffix[x]:
                value = len(prefix[x])
        F[i] = value
    return F


def KMP(T, P):
    F = failure(P)
    i = 0
    j = 0
    if len(P) > len(T):
        return -1
    else:
        while True:
            if i >= len(T):
                return -1
            while P[j] == T[i]:
                i += 1
                j += 1
                if j == len(P):
                    return i - len(P)
            i = i + j - F[j]
            if F[j] == -1:
                j = 0
            else:
                j = F[j]


T = input('Nhập chuỗi T = ')
P = input('Nhập chuỗi P = ')
index = KMP(T, P)
if index == -1:
    print('P không xuất hiện trong T')
else:
    print(f'P xuất hiện trong T ở vị trí {index}')
