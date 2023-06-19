# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, 
# где ключ — значение переданного аргумента, а значение — имя аргумента. 
# Если ключ не хешируем, используйте его строковое представление.


def dict_create(**kwargs):
    result_dict = {}

    for key, value in kwargs.items():
        result_dict[str(value)]= key
    return result_dict
 
    
print(dict_create(lst=1, arg_2=2, arg_3=3))