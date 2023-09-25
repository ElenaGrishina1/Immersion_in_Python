# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. 
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. 
# Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.

import random

my_dict = {"еда": 5, 
           "вода": 5,
           "куртка": 7, 
           "штаны": 8,
           "спальник": 15, 
           "компас": 5,
           "обувь": 5, 
           "посуда": 3}

max_load = 40
count = 0
my_list_things = []
while count < max_load:
    key, value = random.choice(list(my_dict.items()))
    if key in my_list_things:
        continue
    if count + value > max_load:
        break
    count += value
    my_list_things += (str(key), str(value))
print(my_list_things, "=", count)