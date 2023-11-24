number = int(input())
if 0 < number < 10:
    result = number ** 2
elif 10 <= number < 100:
    number_1 = number % 10
    number_2 = number // 10
    print(number_1 * number_2)
elif 100 <= number < 1000:
    number_1 = number % 10
    number_2 = (number // 10) % 10
    number_3 = number // 100
    print(number_1 * 100 + number_2 * 10 + number_3)
else:
    result = 'Введите число из диапазона'

    print(result)
