# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. 
# Программа должна подсказывать «больше» или «меньше» после каждой попытки.

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
num = randint(LOWER_LIMIT, UPPER_LIMIT)
count = 10

while count > 0:
    print(f"Осталось попыток: {count}")
    user_number = int(input("Введите число от 1 до 1000: "))

    if user_number < num:
        print("Больше")
    elif user_number > num:
        print("Меньше")
    elif user_number == num:
        print("Вы угадали!")
        print(f"Программа загадала: {num}")
        break
    count -= 1
    
else:
    print("К сожалению, вы не угадали...")
    print(f"Программа загадала: {num}")



