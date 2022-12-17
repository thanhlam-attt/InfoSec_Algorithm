""" Tính y = a^k mod(N) với k là số mũ lớn
- B1: phân tích k thành số nhị phân (kt...k1k0)
- Đặt A = a
- Nếu k[0] = 0, đặt b = 1
    + Nếu k[0] = 1 đặt b = a
- for i in range(0, t):
    A = A**2 mod(N)
    + Nếu k[i] = 0, b giữ nguyên nên không code đoạn này
    + Nếu k[i] = 1, b = (b * A)mod(N)
- Kết thúc vòng lặp b là kết quả cuối cùng
"""


def Tinh_mod(a, n):
    if a < 0:
        while a < 0:
            a += n
    else:
        while a >= n:
            a -= n
    return a


def Phantich_Nhiphan(n):
    So_Nhiphan = []
    while n > 0:
        sodu = n % 2
        n = n // 2
        So_Nhiphan.append(sodu)
    So_Nhiphan.reverse()
    return So_Nhiphan


def Tinh_Modulo_So_Mu_Lon(a, k, n):
    K = Phantich_Nhiphan(k)
    K.reverse()  # Xét từ phần tử có trọng số bé nhất nên phải đảo lại K
    A = a
    if K[0] == 0:
        b = 1
    else:
        b = a
    for i in range(1, len(K)):
        A = Tinh_mod(A ** 2, n)
        if K[i] == 1:
            b = Tinh_mod(A * b, n)
    return b


a = int(input("Nhập a: "))
k = int(input("Nhập k: "))
n = int(input("Nhập n: "))
print(Tinh_Modulo_So_Mu_Lon(a, k, n))
