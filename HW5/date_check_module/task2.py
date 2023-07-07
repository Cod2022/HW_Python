# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

# Создайте модуль и напишите в нём функцию, которая получает на вход дату в виде строки вида DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
# Проверку года на високосность вынести в отдельную защищённую функцию.

"""
Модуль проверки даты.
"""

from sys import argv


MIN_DAY = 1
MAX_DAY = 31

MIN_MONTH = 1
MAX_MONTH = 12

MIN_YEAR = 1
MAX_YEAR = 9999

FEBRARY = 2

# date = "31.12.2024"

__all__ = ['date_validation', 'terminal_date_input']

def date_validation(date: str):
    day, month, year = map(int, (date.split('.')))
    days_30 = [4, 6, 9, 11]

    if MIN_YEAR < year > MAX_YEAR or MIN_MONTH < month > MAX_MONTH or MIN_DAY < day > MAX_DAY:
        return False
    if month in days_30 and day > 30:
        return False
    if month is FEBRARY and not _leap_year_check(year) and day > 28:
        return False
    if month is FEBRARY and _leap_year_check(year) and day > 29:
        return False
    
    else:
        return True
    
def _leap_year_check(year):
    return not year % 4 != 0 or year % 100 == 0 and year % 400 != 0
        
def terminal_date_input():
    date = argv[1]
    return date

if __name__ == '__main__':
    # date = terminal_date_input() # при запуске из терминала
    print(date_validation(date))






