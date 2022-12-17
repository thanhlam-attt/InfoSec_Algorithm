import math

p = 2147483647
W = 8
m = math.ceil(math.log2(p))
t = math.ceil(m / W)
A = []
B = []
C = []
for i in range(0, t):
    A.append(int(input("Nhập phần tử của mảng A: ")))
for i in range(0, t):
    B.append(int(input("Nhập phần tử của mảng B: ")))

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
