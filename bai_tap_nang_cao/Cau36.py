"""
Câu 36. Lập trình tìm kiếm xâu S1 trong xâu S2 theo thuật toán Boyer-Moore
"""


def last_occurence(T, P):
    L = {}
    for i in range(len(P)):
        if P[i] not in L:
            for j in range(len(P)):
                if P[i] == P[j]:
                    value = j
            L[P[i]] = value

    for i in range(len(T)):
        if T[i] not in L:
            L[T[i]] = -1

    return L


def boyer_moore(T, P):
    L = last_occurence(T, P)
    n = len(T)
    m = len(P)
    i = len(P) - 1
    j = len(P) - 1

    while True:
        if i >= n:
            return -1
        while T[i] == P[j]:
            i -= 1
            j -= 1
            if j == 0:
                return i
        i = i + m - min(j, 1 + L[T[i]])
        j = m - 1


String_T = input('Chuỗi T = ')
String_P = input('Chuỗi P = ')
index = boyer_moore(String_T, String_P)
if index != -1:
    print(f'P xuất hiện trong T từ vị trí : {index}')
else:
    print('P không tồn tại trong T')
