# Реализовать формирование списка, используя функцию range() и возможности генератора.

from functools import reduce

def my_func(previouse_el, el):
    return previouse_el * el

print(f"Четные числа: {[el for el in range(100, 1001) if el % 2 == 0]}")
print(f"Произведение всех элементов списка {reduce(my_func, [el for el in range(100, 1001) if el % 2 == 0])}")

