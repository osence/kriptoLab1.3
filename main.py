# Генерация двух простых чисел A B
# Открытый ключ (Перемножение простых чисел N = A * B)
# Функция эйлера (Fi = (A-1) * (B-1))
# Открытая экспонента (Простое малое число на которое не делиться Fi)
# Секретная экспонента (d = (Fi * k + 1) / e) Нужно подставлять k пока не получится целое число

import random

# Генерируем простые числа до 1000
import sys


def get_primes():
    # Листинг 1
    # вводим N
    n = 1000
    # создаем пустой список для хранения простых чисел
    lst = []
    # в k будем хранить количество делителей
    k = 0
    # пробегаем все числа от 2 до N
    for i in range(2, n + 1):
        # пробегаем все числа от 2 до текущего
        for j in range(2, i):
            # ищем количество делителей
            if i % j == 0:
                k = k + 1
        # если делителей нет, добавляем число в список
        if k == 0:
            lst.append(i)
        else:
            k = 0
    # выводим на экран список
    return lst


# def is_prime(num):
#     if num == 2:
#         return True
#     if num < 2 or num % 2 == 0:
#         return False
#     for n in range(3, int(num ** 0.5) + 2, 2):
#         if num % n == 0:
#             return False
#     return True

def isint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


# Генерация двух простых чисел A B
def generate_prime_numbers():
    sequence = get_primes()
    number1 = random.choice(sequence)
    number2 = random.choice(sequence)
    while number1 == number2:
        number2 = random.choice(sequence)
    pair = (number1, number2)
    return pair


# Открытая экспонента (Простое малое число на которое не делиться Euler)
def generate_open_exponent(fi):
    test_e = 1
    while fi % test_e == 0:
        test_e += 1
    return test_e


# Секретная экспонента (d = (Fi * k + 1) / e) Нужно подставлять k пока не получится целое число
def generate_secret_exponent(fi, open_e):
    k = 1
    secret_e = (fi * k + 1) / open_e
    while secret_e % 1 != 0:
        k += 1
        secret_e = (fi * k + 1) / open_e
    return int(secret_e)


# Генерация цифровой подписи
def generate_s(secret_e, n, m):
    print(m, d ,n)
    return m ** d % n


# Генерация двух простых чисел A B
pairAB = generate_prime_numbers()
p = pairAB[0]
q = pairAB[1]
# Открытый ключ (Перемножение простых чисел N = A * B)
n = p * q
# Функция эйлера (Euler = (A-1) * (B-1))
euler = (p - 1) * (q - 1)
# Открытая экспонента (Простое малое число на которое не делиться Euler)
e = generate_open_exponent(euler)
# Секретная экспонента (d = (Fi * k + 1) / e) Нужно подставлять k пока не получится целое число
d = generate_secret_exponent(euler, e)
print("Открытый ключ:", e, n)

print("Закрытый ключ:", d, n)

# Скрытое сообщение
message = 9999999999 % n

print(sys.maxsize)
# Генерация цифровой подписи
s = generate_s(d, n, message)

print("Цифровая подпись:", s)

deshifr_message = s ** e % n
print("Сверка сообщение", message, deshifr_message)
