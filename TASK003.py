"""
Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
"""
n = int(input("Введите число (n). n =  "))
i = 0
while 2**i <= n:
    print(f"2 в степени {i} = {2**i}")
    i = i+1
