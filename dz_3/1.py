# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.
# [1, 2, 3, 1, 2] -> [1, 2]

list_element = [1, 2, 3, 1, 2, 2, 4, 6, 5, 0]
count = 0
set_list_element = []
for i in list_element:
    for j in list_element:
        if i == j:
            count += 1
            if j not in set_list_element and count > 1:
                set_list_element.append(j)
    count = 0
print(set_list_element)