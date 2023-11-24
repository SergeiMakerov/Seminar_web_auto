# Создайте функцию-генератор. Функция генерирует N простых чисел, начиная с числа
# 2. Для проверки числа на простоту используйте правило:
# “число является простым, если делится нацело только на единицу и на себя”
import typing
def simpl_n(num: int) -> bool:
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# n = 100
# for i in range(2, n):
#     if simpl_n(i):
#         print(i)

def gen_simple(n: int) -> typing.Generator:
    for i in range(2, n):
        if simpl_n(i):
            yield i

# for i in gen_simple(n):
#     print(i)


result = gen_simple(100)
for i in range(5):
    print(next(result))