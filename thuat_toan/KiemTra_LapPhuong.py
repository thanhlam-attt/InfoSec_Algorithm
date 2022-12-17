def check_cube(num):
    root_cube = num ** (1 / 3)
    if round(root_cube) ** 3 == num:
        return True
    else:
        return False


if __name__ == '__main__':
    n = int(input("Nhập n: "))
    if check_cube(n):
        print(f"{n} là lập phương của số: {round(n ** (1 / 3))}")
    else:
        print(f"{n} không là số lập phương")
