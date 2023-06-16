# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. 
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. 
# Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака

camp_items = {'палатка': 3, 'топор': 1, 'котелок': 0.3, 'примус': 1, 
              'аптечка': 1.5, 'спальный мешок': 1.7, 'ботинки': 2, 'куртка': 0.5,
              'термос': 0.5, 'еда': 2,}

BACKPACK_CAPACITY = 10
weight_count = 0

print('Вещи, которые поместятся в рюкзак: ')

for item in camp_items:
    weight_count += camp_items.get(item)
    if weight_count <= BACKPACK_CAPACITY:
        selected_items_total_weight = weight_count
        print(f'{item}: {camp_items.get(item)} кг')

print(f'Общий вес выбранных вещей: {selected_items_total_weight} кг')
print(f'Вместимость рюкзака: {BACKPACK_CAPACITY} кг')