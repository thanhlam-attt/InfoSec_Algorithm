"""Cho mảng A gồm các số nguyên thuộc F_p nhập vào từ bàn phím, hãy viết chương trình in ra mảng B có các phần tử là
nghịch đảo của các phần tử tương ứng trong A. """


def GCD(a, b):
    if a % b == 0:
        return b
    return GCD(b, a % b)


def nghich_dao(a, b):
    if GCD(a, b) != 1:
        return -1
    else:
        y2 = 0
        y1 = 1
        A = a
        while b != 0:
            q = a // b
            r = a % b
            y = y2 - q * y1
            a = b
            b = r
            y2 = y1
            y1 = y
        while y2 < 0:
            y2 += A
        return y2


def mang_nghich_dao(listA, n):
    listB = []
    for loop in range(len(listA)):
        re = nghich_dao(n, listA[loop])
        if re == -1:
            listB.append("Không có")
        else:
            listB.append(nghich_dao(n, listA[loop]))
    return listB


if __name__ == '__main__':
    list_a = []
    num = int(input("Nhập số phần tử của mảng: "))
    for i in range(num):
        a = int(input(f"Nhập A[{i}]: "))
        list_a.append(a)
    list_b = mang_nghich_dao(list_a, num)
    print(list_b)
