# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. 
# Функцию hex используйте для проверки своего результата.

num = input("Введите целое число: ")
num_hex = int(num, base = 16)
print(f"Вы ввели число: {num}")
print(f"Шестнадцатеричное представление числа {num}: {num_hex}")
print(f"Результат проверки преобразованного числа {num} в {num_hex} с помощью hex(): {hex(num_hex)}")
