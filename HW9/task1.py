# Напишите следующие функции:
# Нахождение корней квадратного уравнения
# Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл
import csv
import random


def write_csv_nums(name: str):
    with open(name, 'a', encoding='utf-8', newline='') as f_write:
        csv_write = csv.writer(f_write)
        for _ in range(0, 100):
            res2 = [random.randint(1, 100) for _ in range(1, 4)] 
            csv_write.writerow(res2)



write_csv_nums('nums_csv.csv')
