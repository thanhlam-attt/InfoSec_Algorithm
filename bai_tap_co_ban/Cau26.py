""" Một số được gọi là số mạnh mẽ khi nó đồng thời vừa chia hết cho số nguyên tố và chia hết cho bình phương của số nguyên tố đó.
Tìm số mạnh mẽ nhỏ hơn số N cho trước (N < 10000)."""


def check_number(num):
    if num == 1 or num == 0:
        return False
    prime = [True for loop in range(num)]
    prime[0] = prime[1] = False
    for loop in range(2, num):
        if prime[loop]:
            for j in range(loop * 2, num, loop):
                prime[j] = False
    for loop in range(1, int(num / 2) + 1):
        if prime[loop] and num % loop == 0 and num % (loop ** 2) == 0:
            print(num, "chia hết cho:", loop, " và ", loop ** 2)


if __name__ == '__main__':
    num_N = int(input("Nhập 0 < B < 10000: "))
    while num_N <= 0 or num_N >= 10000:
        num_N = int(input("Nhập Lại 0 < B < 10000: "))

    for i in range(num_N):
        check_number(i)
