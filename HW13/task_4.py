# Вспоминаем задачу из семинара 8 про сериализацию данных,
# где в бесконечном цикле запрашивали имя, личный
# идентификатор и уровень доступа (от 1 до 7) сохраняя
# информацию в JSON файл.
# Напишите класс пользователя, который хранит эти данные в
# свойствах экземпляра.
# Отдельно напишите функцию, которая считывает информацию
# из JSON файла и формирует множество пользователей.
# Реалтзуйте магический метод сравнения пользователей

import json

class User:
    def __init__(self, user_id, name, level):
        self.user_id = user_id
        self.name = name
        self.level = level

    def __str__(self):
        return f'Пользователь: {self.name}\nID: {self.user_id}\nУровень доступа: {self.level}'
    
    # def __eq__(self, other):
    #     return self.user_id == other.user_id and self.name == other.name
        
    

def get_users(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            users_dict = json.load(f)
    except Exception as e:
        print(f'При открытии файла {filename} возникла ошибка {e}')
        return
    print(f'{users_dict = }')
    users = set()
    for level, user in users_dict.items():
        for user_id, name in user.items():
            users.add(User(user_id, name, level))
    return users

if __name__ == '__main__':
    users = get_users('nums_names.json')
    for user in users:
        print(f'{user}\n')





