# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
# n = 5
# 1 2 3 4 5
# x = 3
# -> 1

from random import randint
n = int(input('Введите колчиство элементов в списке: '))
x = int(input('Введите число для подсчета количества вхождений в списке: '))
numbers = [randint(0,9) for i in range(0, n)]

# Вариант № 1
print(numbers)
print(f'Количество вхождений: {numbers.count(x)}')

# Вариант № 2
count = 0
for i in range(0,n):
    if numbers[i] == x: count += 1
print(f'Количество вхождений: {count}')
