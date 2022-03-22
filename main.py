# Генерация двух простых чисел A B
# Открытый ключ (Перемножение простых чисел N = A * B)
# Функция эйлера (Fi = (A-1) * (B-1))
# Открытая экспонента (Простое малое число на которое не делиться Fi)
# Секретная экспонента (d = (Fi * k + 1) / e) Нужно подставлять k пока не получится целое число

import random

P = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 71, 73, 79, 8, 3, 89, 97, 101]
B = 2**32

def generatePrime(border):
    n = random.randint(2, border / 2)
    n = 2 * n - 1
    while not isPrime(n):
        n = random.randint(2, border / 2)
        n = 2 * n - 1
    return n


def isPrime(n):
    for elem in P:
        if n % elem == 0:
            if n == elem:
                return True
            else:
                return False
    r = 100000
    return rabinMiller(n, r)


# Генерация двух простых чисел A B


def rabinMiller(n, r):
    b = n - 1
    betta = bin(b)
    k = -1
    while b > 0:
        k += 1
        betta = betta[:k + 2] + str(b % 2) + betta[k + 3:]
        b = b // 2
    for j in range(r):
        a = random.randint(2, n - 1)
        if euclid(a, n)[0] > 1:
            return False
        d = 1
        for i in range(k, -1, -1):
            x = d
            d = d ** 2 % n
            if (d == 1) and not (x == 1) and not (x == n - 1):
                return False
            if betta[i + 2] == 1:
                d = (d * a) % n
        if not d == 1:
            return False
    return True


def euclid(a, b):
    if a == 0:
        return [b, 0, 1]
    else:
        g, x, y = euclid(b % a, a)
        return [g, y - (b // a) * x, x]


def modExp(a, b, n):
    if b == 0:
        return 1
    if b % 2 == 0:
        x = modExp(a, b // 2, n)
        return x ** 2 % n
    x = modExp(a, (b - 1) // 2, n)
    x = x ** 2 % n
    return (a * x) % n


def modInv(a, b):
    g, x, _ = euclid(a, b)
    if g == 1:
        return x % b
    raise Exception('gcd(a, b) != 1')


# Открытая экспонента (Простое малое число на которое не делиться Euler)
def generate_open_exponent(fi):
    e = generatePrime(2 ** 16)
    while not euclid(fi, e)[0] == 1:
        e = generatePrime(2 ** 16)
    return e


# Секретная экспонента (d = (Fi * k + 1) / e) Нужно подставлять k пока не получится целое число
def generate_secret_exponent(fi, e):
    return modInv(e, fi)


# Генерация цифровой подписи
def generate_s(secret_e, n, m):
    return modExp(m, secret_e, n)


# Скрытое сообщение
message = 2345345345345123
n = 0
q = 0
# Генерация двух простых чисел A B
while message > n:
    p = generatePrime(B)
    while q == p or q == 0:
        q = generatePrime(B)
    n = p * q
print("Выбранные простые числа:", p, q)
# Модуль (Перемножение простых чисел N = A * B)


# Функция эйлера (Euler = (A-1) * (B-1))
fi = (p - 1) * (q - 1)
# Открытая экспонента (Простое малое число на которое не делиться Euler)
e = generate_open_exponent(fi)
# Секретная экспонента (d = (Fi * k + 1) / e) Нужно подставлять k пока не получится целое число
d = generate_secret_exponent(fi, e)
print("Открытый ключ:", e, n)

print("Закрытый ключ:", d, n)

# Генерация цифровой подписи
s = generate_s(d, n, message)
print("Цифровая подпись:", s)

deshifr_message = modExp(s, e, n)
print("Сверка сообщение", message, deshifr_message)
# Результат будет неправильным в случае если открытый ключ n меньше чем сообщение
