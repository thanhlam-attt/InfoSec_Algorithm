""" Một số gọi là số Т-prime nếu có có đúng 3 ước nguyên dương. 
Viết chương trình tìm các số Т-prime nhỏ hơn hoặc bằng N với N cho trước nhập từ bàn phím.
"""


def check_Tprime(num):
    count = 2
    for loop in range(2, int(num / 2) + 1):  # Một nghiệm chỉ có ước ở nửa đầu của nó
        if num % loop == 0:
            count = count + 1
    if count > 3:
        return False
    return count == 3


if __name__ == '__main__':
    n = int(input("Nhập n: "))
    for i in range(1, n + 1):
        if check_Tprime(i):
            print(str(i) + " ", end='')
