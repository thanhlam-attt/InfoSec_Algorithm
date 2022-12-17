# e^x = 1 + ... + x^n/n!

def facto(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * facto(n - 1)


x = int(input("Nhập giá trị x: "))
n = int(input("Nhập giá trị n: "))
Sum = 0
for i in range(0, n + 1):
    Sum += (x ** i) / facto(i)
print(Sum)