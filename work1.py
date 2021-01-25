# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.

from sys import argv

file_name, worked_hours, rate, bonus = argv

wage = (int(worked_hours) * int(rate)) + int(bonus)
print(f"Ваша зарплата составит {wage}")