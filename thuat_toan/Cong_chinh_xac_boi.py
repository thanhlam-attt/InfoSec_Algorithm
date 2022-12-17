import math

p = 2147483647
W = 8
m = math.ceil(math.log2(p))
t = math.ceil(m / W)


def phantich_mang(a):
    listA = []  # Chứa mảng 2^Wt
    listB = []  # Chứa phần tử của a khi viết thành mảng
    for i in range(t - 1, -1, -1):
        listA.append(2 ** (W * i))
    r = a
    for i in range(0, t):
        hso = r // listA[i]
        r = r % listA[i]
        listB.append(hso)
    return listB


# Tính cộng chính xác bội
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
A = phantich_mang(a)
B = phantich_mang(b)
C = []
Truong = 2 ** W
for i in range(0, t):
    C.append(0)

epsi = 0
for i in range(t - 1, -1, -1):
    C[i] = A[i] + B[i] + epsi
    if C[i] >= Truong:
        epsi = 1
        C[i] = C[i] % Truong
    else:
        epsi = 0
        C[i] = C[i]
print("( ", epsi, ", ", C, " )")
