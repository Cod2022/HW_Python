"""
Модуль, который генерирует псевдоимена.
Имя начинется с заглавной буквы,
состоит из 4-7 букв, среди которых есть гласные.
Полученные имена сохраняются в файл.

"""
from random import choice, randint

MIN_LEN = 4
MAX_LEN = 7
VOWELS = 'eyuioa'
CONSONANTS = 'qwrtpsdfghjklzxcvbnm'

def names_gen(names_number, filename):
    name = ''
    for _ in range(names_number):
        letter = choice(VOWELS)
        name += letter.capitalize()
        len = randint(MIN_LEN, MAX_LEN)
        for _ in range(len - 1):
            name += choice(CONSONANTS)
        name += '\n'
    write_names(name, filename)

def write_names(name, filename):
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(name)

        
if __name__=='__main__':
    names_gen(5, 'names.txt')

