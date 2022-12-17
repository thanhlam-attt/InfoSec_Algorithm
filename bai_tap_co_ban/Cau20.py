"""Viết chương trình in ra các cặp số (A,B) nằm trong khoảng (M,N) sao cho ước số chung lớn nhất của A và B có giá
trị là một số D cho trước. Với M,N,D nhập vào từ bàn phím. (0<M,N, D < 1000). """


def gcd(number_a, number_b):
    if number_b == 0:
        return number_a
    return gcd(number_b, number_a % number_b)


def result(number_m, number_n, number_d):
    list_result = []
    for i in range(number_m, number_n + 1):
        for j in range(number_m, number_n + 1):
            if gcd(i, j) == number_d:
                list_result.append((i, j))
    return list_result


number_m = int(input('Nhập số m > 0 = '))
while number_m < 0:
    number_m = int(input('Nhập lại số m > 0 = '))

number_n = int(input(f'Nhập số n > {number_m} = '))
while number_n < number_m:
    number_n = int(input(f'Nhập lại số n > {number_m} = '))

number_d = int(input('Nhập số d = '))
if number_d <= number_n:
    output = result(number_m, number_n, number_d)
    print(output)
else:
    print('Không tồn tại cặp nào')
