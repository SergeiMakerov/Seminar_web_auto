from datetime import date

balance = 0
count = 0
COMMISSION = 0.015
INTEREST_ACCRUED = 0.03
WEALTH_TAX = 0.1
RICHLIMIT = 5_000_000
MINLIMIT = 30
MAXLIMIT = 600
THREEOPERATIONS = 3
MULTIPLES = 50
history = []


def interest_calculation(cash: float) -> None:
    global balance
    global count
    balance += cash
    count += 1
    if count % THREEOPERATIONS == 0:
        balance = balance + INTEREST_ACCRUED * balance
        print("начислены проценты в размере: ", round(INTEREST_ACCRUED * balance, 2))


def bank_operations(cash: float) -> None:
    global balance
    global count
    balance -= cash
    count += 1
    if cash * COMMISSION < MINLIMIT:
        balance -= MINLIMIT
        print("списаны проценты за cash: ", MINLIMIT)
    elif cash * COMMISSION > MAXLIMIT:
        balance -= MAXLIMIT
        print("списаны проценты за cash: ", MAXLIMIT)
    else:
        balance -= cash * COMMISSION
        print("списаны проценты за cash: ", round(cash * COMMISSION, 2))
    if count % THREEOPERATIONS == 0 and count != 0:
        balance = balance + INTEREST_ACCRUED * balance
        print("начислены проценты в размере: ", round(INTEREST_ACCRUED * balance, 2))


def exit_bank():
    print("До свидания!\n")
    exit()


def check_multiples() -> int:
    while True:
        cash = int(input("Введите сумму опреации кратно 50 у.е.\n"))
        if cash % MULTIPLES == 0:
            return cash


while True:
    action = input("1 - снять\n2 - пополнить\n3 - баланс\n4 - история операций\n5 - выйти\n")

    if action == '1':
        if balance > RICHLIMIT:
            balance = balance - balance * WEALTH_TAX
            print("списан налог на богатство: ", round(balance * WEALTH_TAX, 2))
        cash = check_multiples()
        if cash < balance:
            bank_operations(cash)
            history.append([str(date.today()), -1 * cash])
        else:
            print("не достаточно средств\n")
        print("Баланс = ", round(balance, 2))
    elif action == '2':
        cash = check_multiples()
        interest_calculation(cash)
        if balance > RICHLIMIT:
            balance = balance - balance * WEALTH_TAX
            print("списан налог на богатство: ", round(balance * WEALTH_TAX, 2))
        print("Баланс = ", round(balance, 2))
        history.append([str(date.today()), cash])
    elif action == '3':
        print("Баланс = ", round(balance, 2))
    elif action == '4':
        print("История операций: ", history)
    else:
        exit_bank()
