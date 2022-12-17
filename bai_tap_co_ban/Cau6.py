import math


def Tong_Uoc(number):
    tong_so = 0
    for i in range(2, int(math.sqrt(number)) + 1):  # giảm thiểu số lần lặp
        if number % i == 0:
            if number // i == i:
                tong_so = i  # Chỉ cộng một số vì i*i = num
            else:
                tong_so += i + number // i
    return tong_so + 1  # Vì 1 cũng tính là ước


def Check_num(num):
    # ví dụ 220 và 284 thì Tong_uoc(220) = 284 => Tong_uoc(Tong_uoc(220)) = 220 Tong_Uoc(Tong_Uoc(num)) < Tong_Uoc(
    # num) để loại những cặp số hoàn hảo (a, a) hoặc cặp số trùng (a, b) và (b, a)
    flag = 0
    for i in range(2, num):
        if Tong_Uoc(Tong_Uoc(i)) < Tong_Uoc(i) and Tong_Uoc(Tong_Uoc(i)) == i:
            print(Tong_Uoc(Tong_Uoc(i)), " - ", Tong_Uoc(i))
            flag = 1
    if flag == 0:
        print("Không tồn tại cặp số hoàn hảo trong khoảng này")


if __name__ == '__main__':
    num = int(input("Nhập N: "))
    Check_num(num)
