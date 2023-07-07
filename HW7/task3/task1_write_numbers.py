"""
Модуль, которая заполняет файл
(добавляет в конец) случайными парами чисел.
Первое число int, второе - float разделены вертикальной чертой.
Минимальное число - -1000, максимальное - +1000.
Количество строк и имя файла передаются как аргументы функции
"""

from random import randint, uniform

MIN_RANGE = -1000
MAX_RANGE = 1001

def int_float_write(line_numbers, filename):
    with open(filename, 'a', encoding='utf-8') as f:
        for line in range(line_numbers):
            line = f'{randint(MIN_RANGE, MAX_RANGE)} | {uniform(MIN_RANGE, MAX_RANGE):.2f}\n'
            f.write(line)


if __name__=='__main__':
    int_float_write(10, 'numbers.txt')




    