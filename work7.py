# Реализовать формирование списка, используя функцию range() и возможности генератора.

def fibo_gen(n):
    num = 1
    for i in range(1, n + 1):
        num *= i
        yield num


n = int(input(f"Введите факториал какого числа вам нужен: "))
for el in fibo_gen(n):
    print(el)