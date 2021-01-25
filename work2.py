# Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.

import random

my_list = random.sample(range(1, 500), 10)
print(f'Первоначальный список {my_list}')


def numbers(first_list: list):  # Честно помогал брат.
    final_list = []
    for key, value in enumerate(first_list):
        if key+1 < len(first_list) and value < first_list[key+1]:
            final_list.append(first_list[key+1])
    return final_list

print(f'Финальный список{numbers(my_list)}')

#Вариант 2. Не понимаю пока как убрать 300 в начале списка, чтобы его не было как в задании.
print('*'*10)

my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
my_new_list = [el for num, el in enumerate(my_list) if my_list[num - 1] < my_list[num]]
print(f'Первоначальный список {my_list}')
print(f'Финальный список {my_new_list}')

