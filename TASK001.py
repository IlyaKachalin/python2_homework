"""
На столе лежат n монеток. Некоторые из них лежат вверх решкой,
а некоторые – гербом. Определите минимальное число монеток,
которые нужно перевернуть, чтобы все монетки были повернуты
вверх одной и той же стороной. Выведите минимальное количество
монет, которые нужно перевернуть
"""
import random
n = int(input("Введите количество монеток: "))
list = []
for i in range(n):
    from random import randint
    x = random.randint(0, 1)
    list.append(x)
list2 = []
for i in range(n):
    if list[i] == 0:
        t = "р"
        list2.append(t)
    else:
        t = "о"
        list2.append(t)
print(list2)

count_1 = 0
count_2 = 0
for i in range(n):
    if list2[i] == "р":
        count_1 = count_1+1
    else:
        count_2 = count_2+1
if count_2 >= count_1:
    print(f"Перевернуть нужно {count_1} монеток")
else:
    print(f"Перевернуть нужно {count_2} монеток")
