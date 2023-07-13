# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории. 
# Результаты обхода сохраните в файлы json, csv и pickle. 
# Для дочерних объектов указывайте родительскую директорию. 
# Для каждого объекта укажите файл это или директория. 
# Для файлов сохраните его размер в байтах, 
# а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.

import csv
import json
import pickle
import os


def write_dirs_files_json(file_dir):
    with open('root_dir_files.json', 'a', encoding='utf-8') as f_write:
        dir_dict = {}
        for roots, dir, files in os.walk(os.getcwd()):
            dir_dict['roots'] = roots
            dir_dict['dir'] = dir
            dir_dict['files'] = files
            json.dump(dir_dict, f_write, indent=2)

def write_dirs_files_csv(file_dir):
    with open('root_dir_files.csv', 'a', encoding='utf-8', newline='') as f_csv_write:
        csv_write = csv.DictWriter(f_csv_write, fieldnames=["root", "dirs", "files"])

        csv_write.writeheader()
        dir_list = []
        for roots, dir, files in os.walk(os.getcwd()):
            dir_list.append(roots)
            dir_list.append(dir)
            dir_list.append(files)

        print(dir_list)
        csv_write.writerows(dir_list)
        








