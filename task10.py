# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты 
# вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2

n = int(input('Введите количество монеток: '))
zero = 0
one = 0
for i in range(n):
    side = int(input('Какой стороной лежит монетка? (0 - решкой, 1 - гербом): '))
    if side == 0:
        zero+=1
    if side == 1:
        one+=1
if zero <= one:
    print(f'минимальное количество монет, которые нужно перевернуть: {zero}')
else:
    print(f'минимальное количество монет, которые нужно перевернуть: {one}')
