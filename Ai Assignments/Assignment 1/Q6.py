import random as r


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


num = [r.randint(100, 900) for _ in range(100)]

odd_num = []
even_num = []
prime_num = []

for n in num:
    if n % 2 == 0:
        even_num.append(n)
    else:
        odd_num.append(n)

    if is_prime(n):
        prime_num.append(n)

print(odd_num)
print(even_num)
print(prime_num)
