# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. 
# В результирующем списке не должно быть дубликатов.

my_list = [1, 1, "Hi", "Hi", 5, 6, 0.5, 0.5]

ENTERS = 2
result_list = []

for item in set(my_list):
    if my_list.count(item) >= ENTERS:
            result_list.append(item)

print(result_list)