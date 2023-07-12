# Напишите следующие функции:
# Нахождение корней квадратного уравнения
# Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл
import csv
import random
import math
from typing import Callable

NUMBER_OF_ROWS = 100
MIN_NUMBER = -100
MAX_NUMBER = 100
NUMBER_OF_NUMBERS = 3


def write_csv_nums(name: str):
    with open(name, 'w', encoding='utf-8', newline='') as f_write:
        csv_write = csv.writer(f_write)
        for _ in range(0, NUMBER_OF_ROWS):
            res2 = [random.randint(MIN_NUMBER, MAX_NUMBER) for _ in range(0, NUMBER_OF_NUMBERS)] 
            csv_write.writerow(res2)



def read_csv(func: Callable):
    def wrapper(*args, **kwargs):
        with open('nums_csv.csv', 'r', encoding='utf-8', newline='') as f_read:
            csv_read = csv.reader(f_read)
            for line in csv_read:
                int_list = list(map(int, line))
                res_list = func(int_list)
            return res_list
    return wrapper
            


@read_csv
def discriminant_count(lst: list = None):
    a, b, c = lst
    print(f'Числа: {a}, {b}, {c}')
    discr = b ** 2 - 4 * a * c
    print("Дискриминант D = %.2f" % discr)
    if discr > 0:
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
    elif discr == 0:
        x = -b / (2 * a)
        print("x = %.2f" % x)
    else:
        print("Корней нет")

   
write_csv_nums('nums_csv.csv')
discriminant_count()


