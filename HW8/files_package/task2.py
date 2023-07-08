"""
Создание json-файла в формате: {
Уровень доступа: {id:имя}
}
"""

import json
import os

def write_json(file_json):
    if os.path.isfile(file_json):
        with open(file_json, 'r', encoding='utf-8') as f:
            dct = json.load(f)
    else:
        dct = {str(i):{} for i in range(1, 8)}
    
    while True:
        data = input('Введите через пробел имя, ID, уровень доступа: ')
        if not data:
            break
        user_input, id, access = data.split()
        dct.setdefault(access, {id:user_input})[id] = user_input
        
    with open(file_json, 'a', encoding='utf-8') as f:
        json.dump(dct, f, indent=2, ensure_ascii=False)


    


if __name__ == '__main__':
    write_json('nums_names.json')


