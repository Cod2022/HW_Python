# Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК. Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
# * имя файла без расширения или название каталога,
# * расширение, если это файл,
# * флаг каталога,
# * название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя логирование.

import os
import logging
import argparse
from collections import namedtuple


def logger_func(item_obj):
    logging.basicConfig(filename='logs.txt', filemode='a', encoding='utf-8', level=logging.INFO)
    logger = logging.getLogger('Объект каталога')
    logger.info(item_obj)  

def get_dir_objects(dir_arg=None):
    dir = os.listdir(dir_arg)
    Item = namedtuple('Item', ['item_name', 'file_ext', 'dir_flag', 'parent_dir_name'], defaults=[None, False, None])

    for file in dir:
        if os.path.isfile(file):
            file_path, file_ext = os.path.splitext(os.path.abspath(file))
            file_name = os.path.basename(file_path)
            parent_dir = os.path.basename(os.path.dirname(os.path.abspath(file)))
            file_item = Item(file_name, file_ext, parent_dir_name=parent_dir)
            logger_func(file_item)
        elif os.path.isdir(file):
            dir_name = os.path.basename(os.path.abspath(file))
            parent_dir = os.path.basename(os.path.dirname(os.path.abspath(file)))
            dir_item = Item(dir_name, dir_flag=True, parent_dir_name=parent_dir)
            logger_func(dir_item)
        
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Sample') 
    parser.add_argument('-d', help='enter -d or don`t enter anything', action='store_const', const=os.getcwd()) 
    args = parser.parse_args() 
    get_dir_objects(args.d)








