# Представлен список чисел. Определить элементы списка, не имеющие повторений.

from itertools import permutations, repeat, combinations

numbers_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

new = [el for el in numbers_list if numbers_list.count(el) == 1]
print(new)