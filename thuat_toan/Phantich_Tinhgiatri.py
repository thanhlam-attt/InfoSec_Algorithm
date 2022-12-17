# p = 2147483647, W = 8, a = 765432
import math

p = 2147483647
W = 8
m = math.ceil(math.log2(p))
t = math.ceil(m / W)

listA = []  # Chứa mảng 2^Wt
for i in range(t - 1, -1, -1):
    listA.append(2 ** (W * i))


def phantich_mang(a):
    listB = []  # Chứa phần tử của a khi viết thành mảng
    du = a
    for i in range(0, t):
        hso = du // listA[i]
        du = du % listA[i]
        listB.append(hso)
    return listB


def tinhgiatri_mang():
    giatrimang = 0
    listC = []
    for i in range(0, t):
        listC.append(int(input("Nhập các phần tử mảng: ")))
    for i in range(t - 1, -1, -1):
        giatrimang += listA[i] * listC[i]
    return giatrimang


while (1):
    print("1. Nhập số và phân tích thành mảng")
    print("2. Nhập mảng và tính giá trị mảng")
    print("3. Thoát!")
    key = int(input("Chọn số: "))
    if key == 1:
        a = int(input("Nhập a: "))
        listB = phantich_mang(a)
        print("Biểu diễn a dưới dạng mảng là:")
        print(listB)
    if key == 2:
        print("Giá trị của mảng là: ", tinhgiatri_mang())
    if key == 3:
        break
