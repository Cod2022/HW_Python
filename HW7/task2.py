# Напишите функцию группового переименования файлов. Она должна:
# * принимать в качестве аргумента желаемое конечное имя файлов. 

# * При переименовании в конце имени добавляется порядковый номер.

# * принимать в качестве аргумента расширение исходного файла. 
# Переименование должно работать только для этих файлов внутри каталога.

# * принимать в качестве аргумента расширение конечного файла.
# Шаблон переименованного файла: <original_name>_<new_name>_<position>.<new_extention>

import os

def file_rename(new_name, old_extension, new_extension):
    os.chdir('HW7')
    files_list = [_ for _ in os.listdir() if _.endswith(old_extension)]
    for num, file in enumerate(files_list, 1):
        # f = open(file, 'r', encoding='utf-8')
        # line = f.readline()
        # ext_strip = '.' + old_extension
        # print(f'{file.strip(ext_strip)}_{str(num)}')
        strip_old_ext = '.' + old_extension
        new_name_extension = f'{file.strip(strip_old_ext)}_{new_name}_{str(num)}.{new_extension}'
        os.rename(file, new_name_extension)

file_rename("asd", 'txt', 'pdf')
# for item in res:
#     if item.endswith('.txt'):
#             print(item)

