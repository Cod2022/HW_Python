"""
Модуль, которая открывает на чтение созданные
task1_write_numbers и task2_names_generation файлы с числами и именами.
Перемножает пары чисел. В новый файл сохраняет
имя и произведение:
если результат умножения отрицательный, сохраняет имя записанное строчными буквами и произведение по модулю
если результат умножения положительный, сохраняет имя прописными буквами и произведение округлённое до целого.
В результирующем файле столько же строк, сколько в более длинном файле.
При достижении конца более короткого файла,
возвращается в его начало
"""

import math
import os
import typing

def read_per_line(file_obj: typing.TextIO):
    line = file_obj.readline()
    if line == '':
        file_obj.seek(0)
        line = file_obj.readline()

    return line[:-1]


def write_new_file(names, numbers, results):
    len_names = os.path.getsize(names)
    len_numbers = os.path.getsize(numbers)
    with (
        open(names, 'r', encoding='utf-8') as f_names,
        open(numbers, 'r', encoding='utf-8') as f_numbers,
        open(results, 'w', encoding='utf-8') as f_results
        ):
        for _ in range(max(len_names, len_numbers)):
            name = read_per_line(f_names)
            num_line = read_per_line(f_numbers)
            int_num, float_num = num_line.split(' | ')
            res_num = int(int_num) * float(float_num)
            if res_num < 0:
                name = f_names.readline().strip('\n').lower()
                name_num = f'{name}: {str(res_num)}\n'
                f_results.writelines(name_num)
            else:
                res_num = round(res_num)
                name = f_names.readline().strip('\n')
                name_num = f'{name}: {str(res_num)}\n'
                f_results.writelines(name_num)
            

if __name__=='__main__':
    write_new_file('names.txt', 'numbers.txt', 'names_numbers.txt')



       


        