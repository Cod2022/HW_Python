# Напишите следующие функции:
# Нахождение корней квадратного уравнения
# Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл
import csv
import random
from typing import Callable

NUMBER_OF_ROWS = 100
MAX_NUMBER = 100
NUMBER_OF_NUMBERS = 3



def write_csv_nums(name: str):
    with open(name, 'w', encoding='utf-8', newline='') as f_write:
        csv_write = csv.writer(f_write)
        for _ in range(0, NUMBER_OF_ROWS):
            res2 = [random.randint(1, MAX_NUMBER) for _ in range(0, NUMBER_OF_NUMBERS)] 
            csv_write.writerow(res2)

def read_csv_nums(name: str):
    with open(name, 'r', encoding='utf-8', newline='') as f_read:
        csv_read = csv.reader(f_read)
        for line in csv_read:
            int_list = list(map(int, line))
            print(int_list)



write_csv_nums('nums_csv.csv')
read_csv_nums('nums_csv.csv')
