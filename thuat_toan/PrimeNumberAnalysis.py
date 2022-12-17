import math


def CheckPrime(number_check):
    if number_check < 2:
        return 0
    else:
        for loop in range(2, int(math.sqrt(number_check))):
            if number_check % loop == 0:
                return 0
        return 1


def max_listNum(listNumbers):
    max_iter = listNumbers[0]
    for i in range(0, len(listNumbers)):
        if listNumbers[i] > max_iter:
            max_iter = listNumbers[i]
    return max_iter


number = int(input("Nhập giá trị số cần tính: "))
listNumbers = []
loop = 2
while number > 1:
    if CheckPrime(loop) and number % loop == 0:
        number = int(number / loop)
        listNumbers.append(loop)
    else:
        loop = loop + 1
if len(listNumbers) == 0:
    listNumbers.append(number)

listNumbers1 = []
for i in range(0, max_listNum(listNumbers) + 1):
    listNumbers1.append(0)

for i in range(0, len(listNumbers)):
    listNumbers1[listNumbers[i]] += 1

for i in range(0, max_listNum(listNumbers) + 1):
    if listNumbers1[i] != 0:
        print(str(i) + "^" + str(listNumbers1[i]) + " * ", end="")
1