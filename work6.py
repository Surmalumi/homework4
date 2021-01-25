#Реализовать два небольших скрипта:
#итератор, генерирующий целые числа, начиная с указанного;
#итератор, повторяющий элементы некоторого списка, определённого заранее.

from itertools import count, cycle


qty_number = 10
number = 0
for el in count(int(input(f'Введите число, с которого нужно начинать: '))):
    number += 1
    print(el)
    if number >= qty_number:
        number = 0
        break

my_list = ['Дом', 'Снег', 'Сон', 'Сад', 'Плед']

print('*'*10)
for el in cycle(my_list):
    number +=1
    print(el)
    if number >= qty_number:
        number = 0
        break