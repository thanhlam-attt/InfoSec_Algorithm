"""Đặt S1, S2 là các mảng chứa giá trị bình phương của các số nguyên. Hãy viết chương trình in ra số lượng tất cả các
số nguyên tố nằm trong khoảng [a,b] sao cho số này cũng là tổng của hai số x và y với x thuộc S1 và y
thuộc S2. Trong đó, a,b là các số được nhập từ bàn phím Ví dụ: với a=10, b =15,
in ra giá trị là 1 vì trong khoảng [10,15] chỉ có 2 số nguyên tố 11 và 13, nhưng chỉ có 13 = 2^2 + 3^2=4+9. """


def find_num(num_a, num_b):
    s1 = [x * x for x in range(1, num_b + 1)]
    s2 = [y * y for y in range(1, num_b + 1)]
    print("s1 là: ", s1)
    print("s2 là: ", s2)
    for i in range(num_a, num_b):
        for x in range(len(s1)):
            for y in range(len(s2)):
                if i == s1[x] + s2[y] and s1[x] < s2[y]:
                    print(i, " = ", s1[x], " + ", s2[y])


if __name__ == '__main__':
    num_A = int(input("Nhập A: "))
    num_B = int(input(f"Nhập B > {num_A}: "))
    while num_B < num_A:
        num_B = int(input(f"Nhập lại B > {num_A}: "))

    find_num(num_A, num_B)
