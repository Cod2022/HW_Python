# Напишите программу банкомат
# Начальная сумма равна нулю
# Допустимые действия: пополнить, снять, выйти
# Сумма пополнения и снятия кратны 50 руб.
# Процент за снятие - 1.5% от суммы снятия, но не менее 10 и не более 2000 руб.
# После каждой третей операции пополнения или снятия начисляются проценты - 3%
# Нельзя снять больше, чем на счёте
# При превышении суммы в 5млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# Любое действие выводит сумму денег
# Возьмите задачу о банкомате из семинара 
# Разбейте её на отдельные операции — функции. 
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

import datetime


INITIAL_SUM = 0
MIN_COMMISION_LIMIT = 10
MAX_COMISSION_LIMIT = 2000
MULTIPLICITY_SUM = 50

my_balance = 0

def add_money_logs(input_money, balance):
    time_date = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
    log = open('atm_logs.txt', 'a+')
    log.write(f'{time_date}. Пополнение баланса на: {input_money} руб. Баланс: {balance} руб\n')
    log.close()

def extract_money_logs(extraction_sum, commission_rate, balance):
    time_date = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
    log = open('atm_logs.txt', 'a+')
    log.write(f'{time_date}. Снятие: {extraction_sum} руб. Комиссия: {commission_rate} руб. Баланс: {balance} руб\n')
    log.close()

def add_money(balance):
    input_money = int(input('Внесите сумму, кратную 50 руб: '))
    if input_money % MULTIPLICITY_SUM == 0:
        balance += input_money
        print(f'Деньги добавлены.\nВаш баланс: {balance}')
        add_money_logs(input_money,balance)
        return balance
    else:
        print('Ошибка!Внесите сумму, кратную 50 руб!')
        return balance

    

def extract_money(balance):
    print(f'Ваш баланс: {balance:.2f}')
    comission_rate = (balance / 100) * 1.5
    print(f'Комиссия за снятие составит 1.5%, но не менее 10 и не более 2000 руб от суммы снятия')
    extraction_sum = int(input('Введите сумму, которую вы хотите снять:'))
    if comission_rate < MIN_COMMISION_LIMIT:
        balance = balance - extraction_sum - MIN_COMMISION_LIMIT
        print(f'Комиссия за снятие: {MIN_COMMISION_LIMIT} руб')
        print(f'Вы сняли {extraction_sum:.2f} руб.\nВаш баланс: {balance:.2f} руб')
        extract_money_logs(extraction_sum, comission_rate, balance)
        return balance
    elif comission_rate > MAX_COMISSION_LIMIT:
        balance = balance - extraction_sum - MAX_COMISSION_LIMIT
        print(f'Деньги сняты. Ваш баланс: {balance}')
        extract_money_logs(extraction_sum, comission_rate, balance)
        return balance
    elif comission_rate < MAX_COMISSION_LIMIT > MIN_COMMISION_LIMIT:
        balance = balance - extraction_sum - comission_rate
        print(f'Комиссия за снятие: {comission_rate:.2f} руб')
        print(f'Вы сняли {extraction_sum:.2f} руб.\nВаш баланс: {balance:.2f} руб')
        extract_money_logs(extraction_sum, comission_rate, balance)
        return balance
    

def exit_atm(balance):
    print(f'Ваш баланс: {balance}')
    print('До свидания!')


def atm_menu(balance):
    print(f'Ваш баланс: {balance} руб')
    while True:
        choice = input('Выберите: \n1-пополнить счёт\n2-снять деньги\n3-выйти из системы\n')
        match choice:
            case '1':
                balance = add_money(balance)
            case '2':
                balance = extract_money(balance)
            case '3':
                exit_atm(balance)
                break

my_balance=atm_menu(my_balance)



    
