year = int(input('Введите год:'))
MAIN_DIVIDER =4
EXCEPTION_DIVIDER = 100
ADDITIONAL_DIVIDER = 400

if ((year%MAIN_DIVIDER == 0
        and year%EXCEPTION_DIVIDER != 0) \
        or year% ADDITIONAL_DIVIDER == 0):
    print('Год високосный')
else:
    print('Год обычный')