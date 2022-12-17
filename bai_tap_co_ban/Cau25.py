"""Cho 2 số M và N thoả mãn điều kiện: 1<=N<=10000; 2<M<=100; Hãy viết chương trình xác định xem số N có thể được phân
tích thành tổng của M số nguyên tố hay không? Nếu có thì in ra các số đó.
Ví dụ: N=10 và M=3, thì 10=2+3+5 do đó kết quả trả về là thoả mãn và in ra 3 số 2,3,5. """
"""
Câu 25. Cho 2 số M và N thoả mãn điều kiện: 1<=N<=10000; 2<M<=100;
Hãy viết chương trình xác định xem số N có thể được phân tích thành
tổng của M số nguyên tố hay không? Nếu có thì in
ra các số đó.
"""
import math


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


def result(array_prime, subsets, subsetSize, sum, current, target, r):
    """30 => (19,11), (13,17), (7,23)
    array_prime chứa các số ngto từ 1->30
    subsets = (19,11) hoặc (13,17) hoặc (7,23)
    subsetSize là kích thước mảng subsets
    sum = tổng subsets
    current là chỉ số hiện tại
    target = tổng mong muốn = 30
    r là mảng chứa các subsets (19,11), (13,17), (7,23)
    """
    if target == sum:  # nếu tổng hiện tại bằng tổng mục tiêu
        r.append(subsets[0:subsetSize])
        # nếu chỉ số phần tử kế tiếp còn trong biên mảng tập đầu vào và tổng hiện thời trừ phần tử đang xét
        # + tổng phần tử kế tiếp nhỏ hơn tổng mục tiêu
        if current + 1 < len(array_prime) and sum - array_prime[current] + array_prime[current + 1] <= target:
            # tiếp tục đệ quy để tìm tập kết quả tiếp theo, loại bỏ phần tử hiện tại
            result(array_prime, subsets, subsetSize - 1, sum - array_prime[current], current + 1, target, r)

    else:
        # kiểm tra ràng buộc chỉ số phần tử
        if current < len(array_prime) and sum + array_prime[current] <= target:
            # sinh các node dọc theo chiều rộng của mảng đầu vào
            for i in range(current, len(array_prime)):
                subsets[subsetSize] = array_prime[i]
                if sum + array_prime[i] <= target:  # nếu tổng hiện thời với
                    # phần tử đang xét nhỏ hơn hoặc bằng mục tiêu
                    # xem xét tìm tổng tập con của level tiếp theo
                    result(array_prime, subsets, subsetSize + 1,
                           sum + array_prime[i], i + 1, target, r)


if __name__ == '__main__':
    number_n = int(input('Nhập số n = '))
    number_m = int(input('Nhập số M = '))
    array_prime = [i for i in range(2, number_n) if is_prime(i)]
    subsets = [0 for x in range(number_n)]
    r = []
    p = []
    result(array_prime, subsets, 0, 0, 0, number_n, r)
    for e in r:  # In các mảng con
        if len(e) == number_m:
            p.append(e)
    if len(p) != 0:
        for e in p:
            print(e)
    else:
        print("NO")
