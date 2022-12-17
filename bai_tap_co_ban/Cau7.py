""" Một số emirp là một số nguyên tố mà khi đảo ngược vị trí các chữ số của nó, ta cũng được một số nguyên tố. 
Viết chương trình liệt kê các số emirp nhỏ hơn N với N nhập vào từ bàn phím"""


def check_prime(number):
    if number < 2:
        return False
    if number == 2:
        return True
    for loop in range(2, number // 2 + 1):
        if number % loop == 0:
            return False
    return True


def reverse_num(num):
    rev_num = 0
    while num != 0:
        tail = num % 10
        rev_num = rev_num * 10 + tail
        num = num // 10
    return rev_num


if __name__ == '__main__':
    Num = int(input("Nhập N: "))
    for i in range(1, Num):
        if check_prime(i) and check_prime(reverse_num(i)):
            print(i)
