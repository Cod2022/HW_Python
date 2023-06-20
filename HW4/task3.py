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

INITIAL_SUM = 0
MIN_COMMISION_LIMIT = 10
MAX_COMISSION_LIMIT = 2000
MULTIPLICITY_SUM = 50

my_balance = 0

def add_money(balance):
    input_money = int(input('Внесите сумму, кратную 50 руб: '))
    if input_money % MULTIPLICITY_SUM == 0:
        balance += input_money
        print(f'Деньги добавлены.\nВаш баланс: {balance}')
        return balance
    else:
        print('Ошибка!Внесите сумму, кратную 50 руб!')

    

def extract_money(balance):
    if 
    print('Деньги сняты')

def exit_atm(balance):
    print(f'Ваш баланс: {balance}')
    print('До свидания!')


def atm_menu(balance):
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
#print(my_balance)


    
