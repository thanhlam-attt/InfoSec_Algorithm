import math


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        print(i)
        if n % i == 0:
            return False
    return True


print(is_prime(2))
