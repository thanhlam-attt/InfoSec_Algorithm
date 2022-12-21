"""Một số gọi là Q-prime khi nó có đúng 4 ước số nguyên dương.
Hãy viết chương trình in ra các số Q-Prime nhỏ hơn hoặc bằng một số N cho trước nhập từ bàn phím."""


def check_qrime(num):
    count = 2
    for loop in range(2, int(num / 2) + 1):  # Một nghiệm chỉ có ước ở nửa đầu của nó
        if num % loop == 0:
            count = count + 1
    if count == 4:
        retrun True
    return False


if __name__ == '__main__':
    n = int(input("Nhập n: "))
    for i in range(1, n + 1):
        if check_qrime(i):
            print(i, " ", end='')
